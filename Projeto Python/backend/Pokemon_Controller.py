from xml.dom import ValidationErr
from web3 import Web3, HTTPProvider
from util import Constants as constants

class PokemonController:
    def __init__(self):
        self.w3 = Web3(HTTPProvider(constants.PROVIDER_URL))
        print("Is connected? %s" % self.w3.isConnected())
        
        self.contract = self.w3.eth.contract(address=constants.CONTRACT_ADDRESS, abi=constants.CONTRACT_ABI)
        print("Contract found? %s" % ("Yes" if self.contract else "No"))

        self.w3.eth.default_account = self.w3.eth.accounts[0]

        self.owner = self.contract.functions.getOwner().call({
            "from": self.w3.eth.default_account,
        })

    def get_life(self):
        return self.contract.functions.getLife().call({
            "from": self.w3.eth.default_account,
        })

    def change_owner(self, oldOwner, newOwner, contract):
        newOwner = Web3.toChecksumAddress(newOwner)
        nonce = self.w3.eth.getTransactionCount(oldOwner)
        contract = self.w3.eth.contract(address=contract, abi=constants.CONTRACT_ABI)

        print("%s -----> %s" % (oldOwner, newOwner))

        transaction = contract.functions.changeOwner(newOwner).buildTransaction({
            "gasPrice": self.w3.eth.gas_price,
            "chainId": constants.NETWORK_ID,
            "from": oldOwner,
            "nonce": nonce,
        })

        try:
            signed_transaction = self.w3.eth.account.sign_transaction(transaction, private_key=constants.PRIVATE_KEY)
            print(signed_transaction)
            transaction_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
            print(transaction_hash)
            print(Web3.toHex(transaction_hash))
            self.owner = newOwner

            print(("Transaction Hash: %s\n" % transaction_hash))

            return Web3.toHex(transaction_hash), signed_transaction

        except TypeError:
            print("O contrato não pertence ao seu usuário.") 

    def take_damage(self, damage):
        nonce = self.w3.eth.getTransactionCount(self.owner)
        transaction = self.contract.functions.takeDamage(damage).buildTransaction({
            "gasPrice": self.w3.eth.gas_price,
            "chainId": constants.NETWORK_ID,
            "from": self.owner,
            "nonce": nonce,
        })

        try:
            signed_transaction = self.w3.eth.account.sign_transaction(transaction, private_key=constants.PRIVATE_KEY)
            print(signed_transaction)
            transaction_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
            print(transaction_hash)
            print(Web3.toHex(transaction_hash))
        except TypeError:
            print("O contrato não pertence ao seu usuário.") 

    # def get_available_pokemons(self):
    #     block_number = self.w3.eth.get_block_number()
    #     print("Block Number: %s" % block_number)
    #     blocks = []
    #     for i in range(1, block_number):
    #         block = self.w3.eth.get_block(block_identifier=i)
    #         # block = self.w3.eth.get_block(i)
    #         transaction = self.w3.eth.get_transaction_by_block(block)
    #         blocks.append(transaction)

        # print(blocks)
        # return blocks


if __name__ == "__main__":
    pokemon_controller = PokemonController()
    
    oldOwner = Web3.toChecksumAddress(pokemon_controller.w3.eth.accounts[0])
    newOwner = Web3.toChecksumAddress(pokemon_controller.w3.eth.accounts[1])
    print(oldOwner)
    print(newOwner)

    contract = Web3.toChecksumAddress("0x27A69e7C00D775fb73d7c21F92E3fae21ec2e0d2")
    print("Contract: %s" % contract)
    
    # print(pokemon_controller.w3.eth.accounts[1])
    pokemon_controller.change_owner(oldOwner, newOwner, contract)
    # print("Life: %s" % pokemon_controller.get_life())
    # pokemon_controller.take_damage(2)
    # print("Life: %s" % pokemon_controller.get_life())

    # pokemon_controller.get_available_pokemons()
    
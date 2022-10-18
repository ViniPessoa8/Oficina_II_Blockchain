from web3 import Web3, HTTPProvider

# Ganache Data
PROVIDER_URL = "http://127.0.0.1:7545"
CONTRACT_ADDRESS = Web3.toChecksumAddress("0x3770f6DdA9Ce081675e9238F7D1ED5C1C36aceB9")
CONTRACT_ABI = '[ { "inputs": [ { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "uint8", "name": "_attack", "type": "uint8" }, { "internalType": "uint8", "name": "_defense", "type": "uint8" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "oldOwner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "ownerChanged", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "changeOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint8", "name": "damage", "type": "uint8" } ], "name": "takeDamage", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]'
NETWORK_ID = 1337

PRIVATE_KEY = "8f3f7df85339f0a4a0ea68da2786c14a42ebd7bb18f423bc88168c4efe51215b" 

class PokemonController:
    def __init__(self):
        self.w3 = Web3(HTTPProvider(PROVIDER_URL))
        print("Is connected? %s" % self.w3.isConnected())
        
        self.contract = self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
        print("Contract found? %s" % ("Yes" if self.contract else "No"))

        self.w3.eth.default_account = self.w3.eth.accounts[0] 

    def change_owner(self, address):
        newOwner = Web3.toChecksumAddress(address)
        oldOwner = self.contract.functions.getOwner().call({
            "from": self.w3.eth.default_account,
        })
        nonce = self.w3.eth.getTransactionCount(oldOwner)

        print("%s -----> %s" % (oldOwner, newOwner))

        transaction = self.contract.functions.changeOwner(newOwner).buildTransaction({
            "gasPrice": self.w3.eth.gas_price,
            "chainId": NETWORK_ID,
            "from": oldOwner,
            "nonce": nonce,
        })

        signed_transaction = self.w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        print(signed_transaction)
        transaction_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        print(transaction_hash) 

if __name__ == "__main__":
    pokemon_controller = PokemonController()
    print(pokemon_controller.w3.eth.accounts[1])
    newOwner = Web3.toChecksumAddress(pokemon_controller.w3.eth.accounts[0])
    pokemon_controller.change_owner(newOwner)
    
from web3 import Web3, HTTPProvider

# Ganache Data
PROVIDER_URL = "http://127.0.0.1:7545"
CONTRACT_ADDRESS = Web3.toChecksumAddress("0xC18FEad54d592a187624C01E4adcFB5B0e5970fe")
CONTRACT_ABI = '[ { "inputs": [ { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "uint8", "name": "_attack", "type": "uint8" }, { "internalType": "uint8", "name": "_defense", "type": "uint8" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "oldOwner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "ownerChanged", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "changeOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint8", "name": "damage", "type": "uint8" } ], "name": "takeDamage", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]'
NETWORK_ID = 5777

class PokemonController:
    def __init__(self):
        self.w3 = Web3(HTTPProvider(PROVIDER_URL))
        print("Is connected? %s" % self.w3.isConnected())
        self.contract = self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
    
    def test_change_owner(self, address):
        oldOwner = self.contract.functions.getOwner()
        newOwner = Web3.toChecksumAddress(address)

        old_owner_key = self.w3.eth.account.privateKeyToAccount(address)
        acct = old_owner_key.address
        nonce = self.w3.eth.getTransactionCount(acct)
        
        transaction = self.contract.functions.changeOwner(newOwner).buildTransaction({
            "gasPrice": self.w3.eth.gas_price,
            "chainId": NETWORK_ID,
            "from": oldOwner,
            "nonce": nonce,
        })

        old_owner_key = self.w3.eth.account.privateKeyToAccount(oldOwner)
        signed_transaction = self.w3.eth.account.sign_transaction(transaction, private_key = old_owner_key)
        print(signed_transaction)
        transaction_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        print(transaction_hash) 

if __name__ == "__main__":
    pokemon_controller = PokemonController()
    print(pokemon_controller)
    newOwner = str(pokemon_controller.w3.eth.accounts[1])
    print(newOwner)
    pokemon_controller.test_change_owner(newOwner)
    
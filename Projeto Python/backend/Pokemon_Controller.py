from xml.dom import ValidationErr
from web3 import Web3, HTTPProvider
from util import Constants as constants
import Contract_Controller
import json

w3 = Web3(HTTPProvider(constants.PROVIDER_URL))
w3.eth.default_account = constants.USER1_ADDRESS

@staticmethod
def get_life(contract):
    return contract.functions.getLife().call({
        "from": w3.eth.default_account,
    })

@staticmethod
def get_name(contract):
    return contract.functions.getName().call({
        "from": w3.eth.default_account,
    })

@staticmethod
def get_owner(contract):
    return contract.functions.getOwner().call({
        "from": w3.eth.default_account,
    })

@staticmethod
def get_attack(contract):
    return contract.functions.getAttack().call({
        "from": w3.eth.default_account,
    })

@staticmethod
def get_defense(contract):
    return contract.functions.getDefense().call({
        "from": w3.eth.default_account,
    })

@staticmethod
def change_owner(oldOwner, newOwner, contract):
    newOwner = Web3.toChecksumAddress(newOwner)
    nonce = w3.eth.getTransactionCount(oldOwner)
    contract = w3.eth.contract(address=contract, abi=constants.CONTRACT_ABI)

    print("%s -----> %s" % (oldOwner, newOwner))

    transaction = contract.functions.changeOwner(newOwner).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "chainId": constants.NETWORK_ID,
        "from": oldOwner,
        "nonce": nonce,
    })

    try:
        signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=constants.PRIVATE_KEY)
        print(signed_transaction)
        transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        print(transaction_hash)
        print(Web3.toHex(transaction_hash))
        owner = newOwner

        print(("Transaction Hash: %s\n" % transaction_hash))

        return Web3.toHex(transaction_hash), signed_transaction

    except TypeError:
        print("O contrato não pertence ao seu usuário.") 

@staticmethod
def take_damage(damage, contract):
    nonce = w3.eth.getTransactionCount(constants.USER1_ADDRESS)
    transaction = contract.functions.takeDamage(damage).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "chainId": constants.NETWORK_ID,
        # "from": owner,
        "nonce": nonce,
    })

    try:
        signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=constants.PRIVATE_KEY)
        print(signed_transaction)
        transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        print(transaction_hash)
        print(Web3.toHex(transaction_hash))
    except TypeError:
        print("O contrato não pertence ao seu usuário.") 

@staticmethod
def get_all_blocks(self):
    blocks = []
    latest_block = w3.eth.get_block("latest") # latest block
    blocks.append(latest_block["hash"])

    # Get parent block
    parent_hash = w3.toHex(latest_block["parentHash"])
    parent_block = w3.eth.get_block(parent_hash) 
    while(parent_block):
        print("\n%s" % parent_block)
        
        # Gets next block
        parent_hash = w3.toHex(parent_block["parentHash"])
        print("\n%s" % parent_hash)

        # Checks if block has parent
        if parent_hash == constants.ZERO_HASH:
            print("ZERO")
            break
        else:
            blocks.append(parent_block["hash"]) # add block to the list
            parent_block = w3.eth.get_block(parent_hash) # gets next block

    return blocks

@staticmethod
def get_available_pokemons(self):
    pokemons = []
    blocks_hash = get_all_blocks()
    for hash in blocks_hash:
        hash = w3.toHex(hash)

        block = w3.eth.get_block(hash)
        transactions = block["transactions"]
        print(transactions)
        
        for transaction_hash in block["transactions"]:
            t_hash = w3.toHex(transaction_hash) 
            print(t_hash)

            transaction = w3.eth.get_transaction(t_hash)

            _to = transaction["to"]
            print(_to)

            if _to not in pokemons and _to:
                pokemons.append(_to)
            
    return pokemons

if __name__ == "__main__":
    print(w3.api)

    initiated_contract = Contract_Controller.initiate_contract_by_filename("Pokemon", "Pikachu", 10, 9)
    print(get_name(initiated_contract))
# contract.initiate_contract(pok)
# print(contract.get_contracts_abi("Pokemon"))

# pokemons = pokemon_controller.get_available_pokemons()
# print(pokemons)

# for contract_hash in pokemons:
#     contract = pokemon_controller.w3.eth.contract(contract_hash, abi=constants.CONTRACT_ABI)
#     # TODO: GET POKEMON NAME
#     pokemon_name = pokemon_controller.get_name(contract)
#     print(pokemon_name)
    
# oldOwner = Web3.toChecksumAddress(pokemon_controller.w3.eth.accounts[0])
# newOwner = Web3.toChecksumAddress(pokemon_controller.w3.eth.accounts[1])
# print(oldOwner)
# print(newOwner)

# contract = Web3.toChecksumAddress("0x27A69e7C00D775fb73d7c21F92E3fae21ec2e0d2")
# print("Contract: %s" % contract)

# print(pokemon_controller.w3.eth.accounts[1])
# pokemon_controller.change_owner(oldOwner, newOwner, contract)
# print("Life: %s" % pokemon_controller.get_life())
# pokemon_controller.take_damage(2)
# print("Life: %s" % pokemon_controller.get_life())

# pokemon_controller.get_available_pokemons()

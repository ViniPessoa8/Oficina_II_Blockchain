from web3 import Web3, HTTPProvider
from util import Constants as constants
import Contract_Controller

w3 = Web3(HTTPProvider(constants.PROVIDER_URL))
abi = Contract_Controller.get_contract_abi_by_filename("Pokemon")
w3.eth.default_account = w3.eth.accounts[0]

@staticmethod
def initialize_pokemon(name, attack, defense):
    print("\n[INFO] Initializing pokemon on blockchain... (Name: %s, Attack: %s, Defense: %s)" % (name, attack, defense))
    initiated_contract = Contract_Controller.initiate_contract_by_filename("Pokemon", name, attack, defense)
    return initiated_contract

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
def change_owner(oldOwner, newOwner, contract_address):
    print("\n[INFO] Changing pokemon owner... \nPokemon: (%s) \n%s -----------> %s" % (contract_address, oldOwner, newOwner))
    newOwner = Web3.toChecksumAddress(newOwner)
    nonce = w3.eth.getTransactionCount(oldOwner)
    contract = w3.eth.contract(address=contract_address, abi=abi)

    transaction = contract.functions.changeOwner(newOwner).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "chainId": constants.NETWORK_ID,
        "from": oldOwner,
        "nonce": nonce,
    })

    try:
        signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=constants.PRIVATE_KEY)
        transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        owner = newOwner

        print(("Transaction Hash: %s" % w3.toHex(transaction_hash)))

        return Web3.toHex(transaction_hash), signed_transaction

    except TypeError:
        print("O contrato não pertence ao seu usuário.") 

@staticmethod
def take_damage(damage, contract):
    print("\n[INFO] Taking <%s> Damage (%s)" % (damage, contract.address))
    print("Life before damage -> %s" % contract.functions.getLife().call())
    nonce = w3.eth.getTransactionCount(w3.eth.default_account)
    transaction = contract.functions.takeDamage(damage).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "chainId": constants.NETWORK_ID,
        "nonce": nonce,
    })

    try:
        signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=constants.PRIVATE_KEY)
        transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        print("Transaction hash: %s" % w3.toHex(transaction_hash))
    except TypeError:
        print("O contrato não pertence ao seu usuário.") 
    
    print("Life before damage -> %s" % contract.functions.getLife().call())

@staticmethod
def get_all_blocks():
    print("[INFO] Getting all blocks...")
    blocks = []
    latest_block = w3.eth.get_block("latest") # latest block
    blocks.append(latest_block["hash"])

    # Get parent block
    parent_hash = w3.toHex(latest_block["parentHash"])
    parent_block = w3.eth.get_block(parent_hash) 
    while(parent_block):
        # Gets next block
        parent_hash = w3.toHex(parent_block["parentHash"])

        # Checks if block has parent
        if parent_hash == constants.ZERO_HASH:
            break
        else:
            blocks.append(parent_block["hash"]) # add block to the list
            parent_block = w3.eth.get_block(parent_hash) # gets next block

    return blocks

@staticmethod
def get_available_pokemons():
    print("\n[INFO] Getting all available pokemons...")
    pokemons = {}
    blocks_hash = get_all_blocks()
    for hash in blocks_hash:
        hash = w3.toHex(hash)
        block = w3.eth.get_block(hash)

        for transaction_hash in block["transactions"]:
            t_hash = w3.toHex(transaction_hash) 
            transaction = w3.eth.get_transaction(t_hash)
            _to = transaction["to"]

            if _to not in pokemons and _to:
                contract = w3.eth.contract(address=_to, abi=abi)
                try:
                    pokemon_name = get_name(contract)
                    if pokemon_name not in pokemons.keys():
                        print("contract address: %s" % _to, end=" ")
                        print("(%s)" % pokemon_name)
                        pokemons[pokemon_name] = contract
                    else:
                        print("", end="")
                except:
                    pass
        
    return pokemons

if __name__ == "__main__":
    print(w3.api)

    # Creating Contracts
    initialize_pokemon("Charizard", 9, 8)
    initialize_pokemon("Bulbassauro", 6, 5)
    initiated_contract = initialize_pokemon("Pikachu", 10, 9)
    
    # Getting All existing pokemons
    pokemons = get_available_pokemons()
    print("Pokemons: %s" % pokemons)

    # Pokemons Takes Damage
    take_damage(2, initiated_contract)

    # Changes pokemons between owners (PRIVATE KEY must be from the pokemon's owner)
    oldOwner = Web3.toChecksumAddress(w3.eth.accounts[0])
    newOwner = Web3.toChecksumAddress(w3.eth.accounts[1])
    contract = Web3.toChecksumAddress(initiated_contract.address) # Given contract (Need to be deployed). Can be deployed in Remix IDE

    owner_before_transaction = initiated_contract.functions.getOwner().call()
    change_owner(oldOwner, newOwner, contract)
    print("\nContract owner (before transaction): %s" % owner_before_transaction)
    print("Contract owner (after transaction): %s" % initiated_contract.functions.getOwner().call())


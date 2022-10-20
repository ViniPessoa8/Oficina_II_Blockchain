from web3 import Web3, HTTPProvider


class Constants:
    #### Ganache Data ####
    # Privider Info
    PROVIDER_URL = "http://127.0.0.1:7545"
    NETWORK_ID = 1337

    # Contract Info
    CONTRACT_ADDRESS = Web3.toChecksumAddress("0x23953c5c5Ad2bCB9C4aC68C45D627E10588c1FB8")
    CONTRACT_ABI = '[ { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "oldOwner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "ownerChanged", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "changeOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint8", "name": "damage", "type": "uint8" } ], "name": "takeDamage", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "uint8", "name": "_attack", "type": "uint8" }, { "internalType": "uint8", "name": "_defense", "type": "uint8" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "getAttack", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getDefense", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getLife", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getName", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" } ]'

    # Users Info
    PRIVATE_KEY = "9b782aae6de7a90b01804034ec07e4c9a78b1b45f969d06cad23cf2a4d173000" # User 1
    # PRIVATE_KEY = "572ca263ddf4a9b91473384be58148c008e2e489c36f74ab9f0f56e4b6925227" # User 2

    # Misc
    ZERO_HASH = "0x0000000000000000000000000000000000000000000000000000000000000000"
    CONTRACTS_RELATIVE_PATH = "Projeto Python\\contracts\\"
    CONTRACTS_ABSOLUTE_PATH = "C:\\Users\\vinip\\Documents\\Git\\Oficina_II_Blockchain\\Projeto Python\\contracts\\"


from web3 import Web3

class Constants:
    #### Ganache Data ####
    # Privider Info
    PROVIDER_URL = "http://127.0.0.1:7545"
    NETWORK_ID = 1337

    # Contract Info
    CONTRACT_ADDRESS = Web3.toChecksumAddress("0xF4dbb6f3814DAA9045B55BB068318236cFa6cbb0")
    CONTRACT_ABI = '[ { "inputs": [ { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "changeOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint8", "name": "damage", "type": "uint8" } ], "name": "takeDamage", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "uint8", "name": "_attack", "type": "uint8" }, { "internalType": "uint8", "name": "_defense", "type": "uint8" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "oldOwner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "ownerChanged", "type": "event" }, { "inputs": [], "name": "getAttack", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getDefense", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getLife", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" } ]'

    # Users Info
    PRIVATE_KEY = "8f3f7df85339f0a4a0ea68da2786c14a42ebd7bb18f423bc88168c4efe51215b" # User 1
    # PRIVATE_KEY = "572ca263ddf4a9b91473384be58148c008e2e489c36f74ab9f0f56e4b6925227" # User 2
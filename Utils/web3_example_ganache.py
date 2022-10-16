"""
Title: Example of Web3.py using Ganache Server as provider
Author: Vinicius Pessoa

Prerequisites:
    - Web3.py installed (pip install web3)
    - Ganache server installed and running.
    - Set "ganache_server_ip" to your ganache server ip.

Running:
    Simply run the script.
    - If using VSCode: ctrl + F5
"""

from web3 import Web3 

# Initializing server
ganache_server_ip = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_server_ip))

# Users
user1_key = str(w3.eth.accounts[0])
user2_key = str(w3.eth.accounts[1])

# Data to be used in transaction
_data = "data_sample"
_hex_data = w3.toHex(text=_data) # converts data to Hexadecimal

# Transaction Example
transaction = {
    "from": user1_key,
    "to": user2_key,
    "gasPrice": w3.eth.gas_price,
    "data" : _hex_data, # The transaction data MUST be in hexadecimal
    "value": 10,
}

# Main
if __name__ == "__main__":
    # Checking if it's connected to the provider (Ganache)
    print("\nis connected to provider? %s" % w3.isConnected())

    # Accounts
    print("\nAccounts:\n%s" % w3.eth.accounts)

    # Getting Balance from users
    print("User 1 Balance: " + str(w3.eth.get_balance(user1_key)))
    print("User 2 Balance: " + str(w3.eth.get_balance(user2_key)))

    # Making the transaction
    print(w3.eth.send_transaction(transaction))

    # Getting Balance from users
    print("User 1 Balance: " + str(w3.eth.get_balance(user1_key)))
    print("User 2 Balance: " + str(w3.eth.get_balance(user2_key)))

    # Getting the latest block
    latest_block = w3.eth.get_block("latest")
    print("\nLatest block: \n%s" % latest_block)

    # Getting transaction hashes from block property
    _transaction_hashes = latest_block.get("transactions")
    print("\nTransactions Hashes from Block Property:\n%s" % _transaction_hashes)
    _first_transaction_hash = _transaction_hashes[0]
    print("raw transaction hash: %s" % _first_transaction_hash)
    print("Hex transaction hash: %s" % w3.toHex(_first_transaction_hash))
    _transaction = w3.eth.get_transaction(_first_transaction_hash)
    print("First Transaction: %s" % _transaction)


    # Get Transaction
    _transaction = w3.eth.get_transaction("0xdb75511f55254fc91f35a16da114fc540c8ce3427a65e8e3fb68e2b4edb20de3")
    print("\nTransaction:\n" + str(_transaction))
    
    # Gettung the transaction from block
    _transaction = w3.eth.get_transaction_by_block("latest", 0)
    print("\nTransaction From Last Block:\n" + str(_transaction))
    
    # Get data from transaction
    _data = _transaction.get("input")
    print("\nRaw data: %s" % _data)
    _converted_data = w3.toText(hexstr=_data)
    print("Decoded Data: %s" % _converted_data)


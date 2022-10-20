from solcx import install_solc, compile_standard
from web3 import Web3, HTTPProvider
from util import Constants as constants
from time import sleep

_solc_version = "0.8.17"
install_solc(_solc_version)

w3 = Web3(HTTPProvider(constants.PROVIDER_URL))
w3.eth.default_account = w3.eth.accounts[0]

@staticmethod
def open_contract_file(path):
    with open(path, 'r') as file:
        contract_file = file.read()
    
    return contract_file

@staticmethod
def open_contract_file_by_name(filename):
    return open_contract_file(constants.CONTRACTS_ABSOLUTE_PATH + "%s.sol" % filename)

@staticmethod
def compile_contract_file_by_filename(filename):
    contract_file = open_contract_file_by_name(filename)
    return compile_contract_file(contract_file)

@staticmethod
def compile_contract_file(contract_file):
    compiled_solidity = compile_standard(
        {
            "language": "Solidity",
            "sources": {"Projeto Python\\contracts\\Pokemon.sol": {"content": contract_file}},
            "settings": {
                "outputSelection": {
                    "*": {
                            "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                            # "*": ["abi", "bin"]
                    }
                }
            },
        },
        solc_version=_solc_version,
    )
    return compiled_solidity

@staticmethod
def get_contract_abi_from_compiled_solidity(compiled_solidity):
    abis = []
    for key in compiled_solidity.keys():
        abi = compiled_solidity[key]['abi']

        abis.append((key, abi))
    
    return abis

@staticmethod
def get_contract_bytecode_from_compiled_solidity(compiled_solidity):
    res = compiled_solidity["contracts"]["Projeto Python\\contracts\\Pokemon.sol"]["Pokemon"]["evm"]["bytecode"]["object"]
    return res

@staticmethod
def get_contract_abi_by_filename(filename):
    contract_file = open_contract_file(constants.CONTRACTS_ABSOLUTE_PATH + "%s.sol" % filename)
    compiled_solidity = compile_contract_file(contract_file)
    
    return get_contract_abi(compiled_solidity)

@staticmethod
def get_contract_abi(compiled_solidity):
    res = compiled_solidity["contracts"]["Projeto Python\\contracts\\Pokemon.sol"]["Pokemon"]["abi"]
    return res

@staticmethod
def initiate_contract(compiled_contract, *args):
    bytecode = get_contract_bytecode_from_compiled_solidity(compiled_contract)
    abi = get_contract_abi(compiled_contract)

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    
    nonce = w3.eth.get_transaction_count(w3.eth.default_account)
    construct_txn = contract.constructor(*args).buildTransaction(
        {
            "gasPrice": w3.eth.gas_price, 
            "chainId": constants.NETWORK_ID, 
            "from": w3.eth.default_account, 
            "nonce": nonce
        }
    )
    tx_create = w3.eth.account.sign_transaction(construct_txn, constants.PRIVATE_KEY)
    # tx_hash = contract.constructor(*args).transact({"from": constants.USER1_ADDRESS})
    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # sleep(10)
    print("TX RECEIPT -------------> %s" % tx_receipt)

    return w3.eth.contract(tx_receipt["contractAddress"], abi=abi)

@staticmethod
def initiate_contract_by_filename(filename, *args):
    compiled_contract = compile_contract_file_by_filename(filename)
    return initiate_contract(compiled_contract, *args)

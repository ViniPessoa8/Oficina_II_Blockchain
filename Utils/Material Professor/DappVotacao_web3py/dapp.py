import json
from web3 import Web3, HTTPProvider
#from web3.contract import ConciseContract

from pywebio.input import input
from pywebio.output import put_text, put_image, use_scope, clear


# web3.py instance
w3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/e8c1376f04e245fc8286ae1cd76c6977"))
print(w3.isConnected())

chain_id = 4 #id da rede Rinkbey
contract_address = Web3.toChecksumAddress("0xa621Be3C424e633260ddAB06B6F2E03Eb0450a53")
abi = json.loads('[ { "inputs": [ { "internalType": "address", "name": "_eleitor", "type": "address" } ], "name": "registrarEleitor", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "string", "name": "_candidato", "type": "string" } ], "name": "votar", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "candidatos", "outputs": [ { "internalType": "string", "name": "nome", "type": "string" }, { "internalType": "uint256", "name": "qtDeVotos", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "eleitores", "outputs": [ { "internalType": "address", "name": "idEleitor", "type": "address" }, { "internalType": "bool", "name": "statusDoVoto", "type": "bool" } ], "stateMutability": "view", "type": "function" } ]')


# Contract instance
contract_instance = w3.eth.contract(abi=abi, address=contract_address)
totalDeVotos = 0

    
def votar(candidato, chave):
    
    acct = w3.eth.account.privateKeyToAccount(chave)
    account_address= acct.address
    print(account_address)
    nonce = w3.eth.getTransactionCount(account_address)
    print(nonce)
    # Wait for transaction to be mined
    transaction = contract_instance.functions.votar(candidato).buildTransaction(
        {
            "gasPrice": w3.eth.gas_price,
            "chainId": chain_id,
            "from": account_address,
            "nonce": nonce 
        }
    )
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key = chave)
    print(signed_transaction)
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print(transaction_hash)
    with use_scope('A'):
        put_image(open('foo.png', 'rb').read())
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)   
    
    
def obterVotos(id_candidato):
    totalDeVotos = contract_instance.functions.candidatos(id_candidato).call()
    return totalDeVotos

def mostrarTotalDeVotos():
    clear('A')
    ListaDeVotosDeCandidatos = ""
    for i in range(6):            
        ListaDeVotosDeCandidatos = ListaDeVotosDeCandidatos + str(obterVotos(i)) +"\n"
         
    put_text("Total de Votos de cada candidato").style('color: red; font-size: 40px')
    put_text(ListaDeVotosDeCandidatos).style('color: blue; font-size: 20px')

def main():
    chave = input("Digite sua chave de acesso：")
    candidato = input("Digite o nome do candidato：")
    
    votar(candidato,chave)    
    mostrarTotalDeVotos()
    
          
if __name__ == '__main__':
    main()

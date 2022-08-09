from Blockchain import Blockchain
# from UI import show_trade_form
from SmartContract import SmartContract
from Transaction import Transaction


def main():
    blockchain = Blockchain(2)
    sc = SmartContract(blockchain)
    transaction = Transaction("Ash", "Garry", "Pikachu")
    sc.makeTransaction(transaction)
    print(sc.getData())
    print(blockchain.toString())
    # blockchain = bc.Blockchain(2)
    # blockchain.addBlock(blockchain.newBlock("Tout sur le Bitcoin"))
    # blockchain.addBlock(blockchain.newBlock("Sylvain Saurel"))
    # blockchain.addBlock(blockchain.newBlock("https://www.toutsurlebitcoin.fr"))
    
    # print("Blockchain valid ? " + str(blockchain.isBlockChainValid()))
    
main()
# show_trade_form()
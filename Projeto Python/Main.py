import Blockchain as bc
from UI import show_trade_form



def main():
    blockchain = bc.Blockchain(2)
    blockchain.addBlock(blockchain.newBlock("Tout sur le Bitcoin"))
    blockchain.addBlock(blockchain.newBlock("Sylvain Saurel"))
    blockchain.addBlock(blockchain.newBlock("https://www.toutsurlebitcoin.fr"))
    
    print("Blockchain valid ? " + str(blockchain.isBlockChainValid()))
    print(blockchain.toString())
    

show_trade_form()
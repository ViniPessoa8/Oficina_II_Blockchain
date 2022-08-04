import Blockchain as bc

def main():
    blockchain = bc.Blockchain(4)
    blockchain.addBlock(blockchain.newBlock("Tout sur le Bitcoin"))
    blockchain.addBlock(blockchain.newBlock("Sylvain Saurel"))
    blockchain.addBlock(blockchain.newBlock("https://www.toutsurlebitcoin.fr"))
    
    print("Blockchain valid ? " + str(blockchain.isBlockChainValid()))
    print(blockchain.toString())
    
main()
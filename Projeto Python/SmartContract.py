from Blockchain import Blockchain
from Transaction import Transaction
# import Controller as ctrl
import streamlit as st

# ctrl.initialize_session()
# data = st.session_state['data']

class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        # self.getData()
    
    def getData(self):

        self.data = st.session_state['data']

        out = ""
        for key in self.data.keys():
            out += key + ": " + str(self.data[key].pokemons) + "\n"
        return out
    
    def makeTransaction(self, transaction):
        self.getData()
        newBlock = self.blockchain.newBlock(transaction)
        self.blockchain.addBlock(newBlock)
        
        if self.blockchain.isBlockChainValid():
            self.data[transaction.sender].removePokemon(transaction.pokemon)
            self.data[transaction.receiver].addPokemon(transaction.pokemon)
    
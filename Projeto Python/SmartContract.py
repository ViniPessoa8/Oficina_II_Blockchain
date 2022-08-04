from Blockchain import Blockchain
from Transaction import Transaction
import streamlit as st

data = st.session_state['data']

class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain
    
    def getData(self):

        st.session_state['data'] = data

        out = ""
        for key in data.keys():
            out += key + ": " + str(data[key].pokemons) + "\n"
        return out
    
    def makeTransaction(self, transaction):
        newBlock = self.blockchain.newBlock(transaction)
        self.blockchain.addBlock(newBlock)
        
        if self.blockchain.isBlockChainValid():
            data[transaction.sender].removePokemon(transaction.pokemon)
            data[transaction.receiver].addPokemon(transaction.pokemon)
    
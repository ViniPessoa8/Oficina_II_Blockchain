import streamlit as st
from Treinador import Treinador
from Blockchain import Blockchain
from SmartContract import SmartContract
from Transaction import Transaction

SESSION_DATA = 'data'
SESSION_LOG = 'log'
PATH_IMG_POKEBOLA = "res\pokebola.png"

blockchain = Blockchain(2)
sc = SmartContract(blockchain)

if SESSION_DATA in st.session_state:
    del st.session_state[SESSION_DATA]

def initialize_session():

    if SESSION_LOG not in st.session_state: 
        st.session_state[SESSION_LOG] = ''

    if SESSION_DATA not in st.session_state:
        st.session_state['data'] = {
            "Ash":      Treinador(1, ["Pikachu", "Bulbasaur"]),
            "Garry":    Treinador(2, ["Raichu", "Ivysaur"]),
            "Lais":     Treinador(3, ["Rattata", "Bulbasaur", "Riolu", "Squirtle"]),
            "Vini":     Treinador(4, ["Charmander", "Bulbasaur", "Mewtwo"]),
            "Veronica": Treinador(5, ["Squirtle", "Bulbasaur"]),
            "Tersio":   Treinador(6, ["Eevee", "Bulbasaur"])
        }

def trocar(nome_treinador_01, nome_treinador_02, id_pokemon):

    global pokedata

    transaction = Transaction(nome_treinador_01, nome_treinador_02, id_pokemon)
    sc.makeTransaction(transaction)
    sc.getData()
    # st.write(blockchain.toString())

    pokedata = st.session_state[SESSION_DATA]

    st.session_state[SESSION_LOG] = blockchain.toString()

    st.experimental_rerun()
    
initialize_session()
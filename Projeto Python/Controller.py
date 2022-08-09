import streamlit as st
from Treinador import Treinador
from Blockchain import Blockchain
from SmartContract import SmartContract
from Transaction import Transaction

SESSION_DATA = 'data'
SESSION_LOG = 'log'

def initialize_session():

    if SESSION_LOG not in st.session_state: 
        st.session_state[SESSION_LOG] = ''

    if SESSION_DATA not in st.session_state:
        st.session_state['data'] = {
            "Ash":      Treinador(1, ["Pikachu", "Bulbasaur"]),
            "Garry":    Treinador(2, ["Raichu", "Ivysaur"]),
            "Lais":     Treinador(3, ["Ratata", "Bulbasaur"]),
            "Vini":     Treinador(4, ["Charmamder", "Bulbasaur"]),
            "Veronica": Treinador(5, ["Squirtle", "Bulbasaur"]),
            "Tersio":   Treinador(6, ["Eevee", "Bulbasaur"]),
            "Eca":      Treinador(7, ["Riolu", "Bulbasaur"]),
            "Poppi":    Treinador(8, ["Mewtwo", "Bulbasaur"])
        }
    
    pokedata = st.session_state[SESSION_DATA]
    nomes_treinadores = pokedata.keys()

def trocar(nome_treinador_01, nome_treinador_02, id_pokemon):

    global pokedata

    blockchain = Blockchain(2)
    sc = SmartContract(blockchain)
    transaction = Transaction(nome_treinador_01, nome_treinador_02, id_pokemon)
    sc.makeTransaction(transaction)
    sc.getData()
    # st.write(blockchain.toString())

    pokedata = st.session_state[SESSION_DATA]

    st.session_state[SESSION_LOG] = blockchain.toString()

    st.experimental_rerun()
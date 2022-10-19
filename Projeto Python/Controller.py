from mimetypes import init
from pydoc import text
import streamlit as st
import requests
from Blockchain import Blockchain
from SmartContract import SmartContract
from Transaction import Transaction
import backend.Pokemon_Controller as pc


SESSION_DATA = 'data'
SESSION_LOG = 'log'
PATH_IMG_POKEBOLA = "res\pokebola.png"

blockchain = Blockchain(2)
sc = SmartContract(blockchain)
pokemonController = pc.PokemonController()

# if SESSION_DATA in st.session_state:
#     del st.session_state[SESSION_DATA]

# blockchain = Blockchain(2)
# sc = SmartContract(blockchain)

def initialize_session():

    if SESSION_LOG not in st.session_state: 
        st.session_state[SESSION_LOG] = ''

    if SESSION_DATA not in st.session_state:
        st.session_state[SESSION_DATA] = {
            "Ash":      Treinador(1, ["Pikachu", "Bulbasaur"]),
            "Garry":    Treinador(2, ["Raichu", "Ivysaur"]),
            "Lais":     Treinador(3, ["Rattata", "Geodude", "Riolu", "Squirtle"]),
            "Vini":     Treinador(4, ["Charmander", "Greninja", "Mewtwo"]),
            "Veronica": Treinador(5, ["Lugia", "Charizard"]),
            "Tersio":   Treinador(6, ["Eevee", "Alakazam"])
        }

def trocar(nome_treinador_01, nome_treinador_02, id_pokemon):
    global pokedata

    transaction = Transaction(nome_treinador_01, nome_treinador_02, id_pokemon)
    sc.makeTransaction(transaction)
    sc.getData()

    pokedata = st.session_state[SESSION_DATA]

    # st.session_state[SESSION_LOG] = blockchain.toString()

    st.experimental_rerun()

def _trocar(user1, user2, contract_address):
    hash, transaction = pokemonController.change_owner(user1, user2, contract_address)
    st.session_state[SESSION_LOG] = "Transaction Hash: %s\nTransaction: %s\n" % (hash, transaction)
    
def show_trade_form():
    pokedata = st.session_state[SESSION_DATA]
    nomes_treinadores = pokedata.keys()

    id_treinador_01 = st.text_input(label="Treinador 01", value = "0xC18FEad54d592a187624C01E4adcFB5B0e5970fe", placeholder="0xC18FEad54d592a187624C01E4adcFB5B0e5970fe")
    id_pokemon = st.text_input(label="select a Pokemon", value = "0x27A69e7C00D775fb73d7c21F92E3fae21ec2e0d2", placeholder="0x27A69e7C00D775fb73d7c21F92E3fae21ec2e0d2")

    nomes_sem_treinador_01 = list(filter(lambda x: x != id_treinador_01, nomes_treinadores))

    id_treinador_02 = st.text_input(label="Treinador 02", value = "0x961814Ab5a9abD02a557Fb3cade72e864bfbea84", placeholder="0x961814Ab5a9abD02a557Fb3cade72e864bfbea84")
    
    col_1, col_2, _, col_4 = st.columns(4)

    with col_1:
        if st.button("E N V I A R"):
            # trocar(id_treinador_01, id_treinador_02, id_pokemon)
            _trocar(id_treinador_01, id_treinador_02, id_pokemon)
    with col_2:
        if st.button("Show Log"):
            show_blockchain_log()

          
def _show_blockchain_log():
    log = st.session_state[SESSION_LOG]
    st.write(log if log else "No log available.")

def show_blockchain_log():

    log = st.session_state[SESSION_LOG]

    count = 0
    log = log.split('\n')
    for line in log:
        # st.write(f"Block #{count}")
        count += 1
        line = line[line.find("[")+1:line.find("]")]
        line = line.split(',')
        
        for log_data in line:
            st.write(log_data)
        else:
            st.write("---------")
    
    
    
    # Block #0 [previousHash : 0, timestamp : 1659589335.969274, data : Genesis Block, Nonce : 220] Block #1 [previousHash : 002d86ef185cc273cd032c184cb52e2a013b7dfc0ed94d684d111d87addea33c, timestamp : 1659589335.972266, data : <Transaction.Transaction object at 0x000002425315F2E0>, Nonce : 617]
    pass

def get_sprite_url(pokemon_name):
    api = f"https://pokeapi.glitch.me/v1/pokemon/{pokemon_name}"
    res = requests.get(api)

    url = 'foi nao'

    try:
        res = res.json()
        return res[0]["sprite"]
    except:
        url = PATH_IMG_POKEBOLA
        return url

# initialize_session()

from Treinador import Treinador
import streamlit as st
from Treinador import data as pokedata

nomes_treinadores = pokedata.keys()

st.title("PokeTrader")

def trocar(nome_treinador_01, nome_treinador_02, id_pokemon):
    id_treinador_01 = pokedata[nome_treinador_01].id
    id_treinador_02 = pokedata[nome_treinador_02].id
    

    st.write(nome_treinador_01, nome_treinador_02, id_pokemon)
    return "Olha se num é um hash aqui -> 0000002892jbf27984rjhn92"

def show_trade_form():

    id_treinador_01 = st.selectbox(label="Treinador 01", options=nomes_treinadores)
    id_pokemon = st.selectbox(label="select a Pokemon", options=pokedata[id_treinador_01].pokemons)

    nomes_sem_treinador_01 = list(filter(lambda x: x != id_treinador_01, nomes_treinadores))

    id_treinador_02 = st.selectbox(label="Treinador 02", options=nomes_sem_treinador_01)

    if st.button("E N V I A R"):
        st.write(trocar(id_treinador_01, id_treinador_02, id_pokemon))


show_trade_form()


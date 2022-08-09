import streamlit as st
import Controller as control

data = st.session_state[control.SESSION_DATA]

def print_trainer(name = "Ash"):
    global data
    
    st.header(name)
    
    pokemons = data[name].pokemons 

    cols = st.columns(6)

    for i in range(len(pokemons)):
        with cols[i]:
            st.write(pokemons[i])

for name in data.keys():
    print_trainer(name)


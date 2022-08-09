import streamlit as st
import Controller as control
import requests

# control.reset_session()
control.initialize_session()
data = control.st.session_state[control.SESSION_DATA]


def print_trainer(name = "Ash"):
    global data
    data = st.session_state[control.SESSION_DATA]
    
    st.header(name)
    
    pokemons = data[name].pokemons 

    cols = st.columns(6)

    for i in range(len(pokemons)):
        with cols[i]:
            st.write(pokemons[i])
            st.image(control.get_sprite_url(pokemons[i]), width=50)

for name in data.keys():
    print_trainer(name)


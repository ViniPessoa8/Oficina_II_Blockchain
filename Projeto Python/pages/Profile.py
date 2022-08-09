import streamlit as st
import Controller as control
import requests

# control.reset_session()
control.initialize_session()
data = control.st.session_state[control.SESSION_DATA]

def get_sprite_url(pokemon_name):
    api = f"https://pokeapi.glitch.me/v1/pokemon/{pokemon_name}"
    res = requests.get(api)

    url = 'foi nao'

    try:
        res = res.json()
        return res[0]["sprite"]
    except:
        url = control.PATH_IMG_POKEBOLA
        return url


def print_trainer(name = "Ash"):
    global data
    data = st.session_state[control.SESSION_DATA]
    
    st.header(name)
    
    pokemons = data[name].pokemons 

    cols = st.columns(6)

    for i in range(len(pokemons)):
        with cols[i]:
            st.write(pokemons[i])
            st.image(get_sprite_url(pokemons[i]), width=50)

for name in data.keys():
    print_trainer(name)


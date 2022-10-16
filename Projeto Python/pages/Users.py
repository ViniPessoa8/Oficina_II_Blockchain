import streamlit as st
import Controller as control

control.initialize_session()

data = control.st.session_state[control.SESSION_DATA]

def print_trainer(name = "Ash"):
    st.subheader(name)
    global data
    data = st.session_state[control.SESSION_DATA]
    pokemons = data[name].pokemons 
    cols = st.columns(6)
    
    
    if len(pokemons) == 0:
        st.write("(No pokemons)")
    else:
        for i in range(len(pokemons)):
            with cols[i]:
                st.write(pokemons[i])
                st.image(control.get_sprite_url(pokemons[i]), width=50)


st.header("Users")
for name in data.keys():
    print_trainer(name)

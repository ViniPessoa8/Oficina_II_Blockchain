import streamlit as st

data = None
class treinador:
    def __init__(self, id: int, pokemons=[]):
        self.id = id
        self.pokemons = pokemons

    def addPokemon(self, pokemon):
        if pokemon not in (None, ''):
            self.pokemons.append(pokemon)

    def removePokemon(self, pokemon):
        if pokemon not in (None, ''):
            self.pokemons.remove(pokemon)

def update_data():
    data = st.session_state['data']

if 'data' not in st.session_state:
    st.session_state['data'] = {
        "Ash":      treinador(1, ["Pikachu", "Bulbasaur"]),
        "Garry":    treinador(2, ["Raichu", "Ivysaur"]),
        "Lais":     treinador(3, ["Ratata", "Bulbasaur"]),
        "Vini":     treinador(4, ["Charmamder", "Bulbasaur"]),
        "Veronica": treinador(5, ["Squirtle", "Bulbasaur"]),
        "Tersio":   treinador(6, ["Eevee", "Bulbasaur"]),
        "Eca":      treinador(7, ["Riolu", "Bulbasaur"]),
        "Poppi":    treinador(8, ["Mewtwo", "Bulbasaur"])
    }

update_data()
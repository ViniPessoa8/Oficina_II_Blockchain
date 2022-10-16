import streamlit as st
import Controller as ctrl


data = None
class Treinador:
    def __init__(self, id: int, pokemons=[]):
        # ctrl.initialize_session()
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

# if 'data' not in st.session_state:
#     st.session_state['data'] = {
#         "Ash":      Treinador(1, ["Pikachu", "Bulbasaur"]),
#         "Garry":    Treinador(2, ["Raichu", "Ivysaur"]),
#         "Lais":     Treinador(3, ["Ratata", "Bulbasaur"]),
#         "Vini":     Treinador(4, ["Charmamder", "Bulbasaur"]),
#         "Veronica": Treinador(5, ["Squirtle", "Bulbasaur"]),
#         "Tersio":   Treinador(6, ["Eevee", "Bulbasaur"]),
#         "Eca":      Treinador(7, ["Riolu", "Bulbasaur"]),
#         "Poppi":    Treinador(8, ["Mewtwo", "Bulbasaur"])
    # }
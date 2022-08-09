import streamlit as st
import Controller as ctrl

ctrl.initialize_session()

st.header("Trade Page")

pokedata = st.session_state[ctrl.SESSION_DATA]
nomes_treinadores = pokedata.keys()

ctrl.show_trade_form()


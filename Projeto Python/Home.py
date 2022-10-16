import streamlit as st
import Controller as ctrl

ctrl.initialize_session()

st.title("Pokemon tradder with Blockchain")

# profile_button = st.button("Trade Page", on_click=ctrl.show_trade_form)
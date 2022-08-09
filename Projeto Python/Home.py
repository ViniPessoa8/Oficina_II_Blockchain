from cProfile import Profile
import streamlit as st
import Controller as ctrl
import pages.Profile as profile

ctrl.initialize_session()

# profile_button = st.button("Trade Page", on_click=ctrl.show_trade_form)
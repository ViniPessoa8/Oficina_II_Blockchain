import streamlit as st
import Controller as ctrl
import pandas as pd

ctrl.initialize_session()

pokedata = st.session_state[ctrl.SESSION_DATA]
users = pokedata.keys() 


transactions = ctrl.blockchain.blocks
for index, transaction in enumerate(transactions):
    if transaction.getData() == "Genesis Block":
        continue
    
    container = st.container()
    column1, column2, column3, column4, column5 = st.columns(5)
    
    with container:
        st.write("%s : %s" % (index,transaction.hash))
        
        with column1:
            st.subheader(transaction.getData().sender)
        
        with column2:
            st.image("res/arrow.png", width=50)
        
        with column3:
            pokemon_name = transaction.getData().pokemon
            st.image(ctrl.get_sprite_url(pokemon_name), width=50)
        
        with column4:
            st.image("res/arrow.png", width=50)
        
        with column5:
            st.subheader(transaction.getData().receiver)
    
        
    
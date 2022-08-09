import streamlit as st
import Controller as ctrl
import pandas as pd

ctrl.initialize_session()

pokedata = st.session_state[ctrl.SESSION_DATA]
users = pokedata.keys() 

# df = pd.DataFrame(data=(pokemons for pokemons in (users_pokemons for users_pokemons in (pokedata[user].pokemons for user in users))), 
#                   index=(name for name in users))

transactions = ctrl.blockchain.blocks
if len(transactions) > 1:
    df = pd.DataFrame(data=(transaction.getData().sender for transaction in transactions if transaction.getData() != "Genesis Block"))
    st.table(df)

# for element in users:
#     user_txt = element + ": "
    
#     for pokemon in pokemons:
#         user_txt += "%s, " % pokemon
    
#     st.write(user_txt)
    # st.table(df)

# st.dataframe(pokedata)
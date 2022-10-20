from cgitb import text
from re import sub
import streamlit as st
import Controller as ctrl

ctrl.initialize_session()

st.title("Pokemon tradder with Blockchain")

def init_login_form():
    
    with st.form():
        
        txt_pkey = ''

        if ctrl.SESSION_PRIVATE_KEY in st.session_state:
            txt_pkey = st.session_state[ctrl.SESSION_PRIVATE_KEY]

        input_private_key = st.text_input(label="Key", placeholder="Insert your private key", value=txt_pkey)
        submit = st.form_submit_button("logar")

        if submit:
            st.cache
            st.session_state[ctrl.SESSION_LOG_IN] = True
            st.session_state[ctrl.SESSION_PRIVATE_KEY] = input_private_key

# @st.cache(suppress_st_warning=True)
def get_private_key():
    return st.session_state[ctrl.SESSION_PRIVATE_KEY]


if ctrl.SESSION_LOG_IN in st.session_state:
    pkey = ctrl.SESSION_PRIVATE_KEY
    st.write("USER LOGGED IN")
    st.write(pkey)
else: init_login_form()


# profile_button = st.button("Trade Page", on_click=ctrl.show_trade_form)
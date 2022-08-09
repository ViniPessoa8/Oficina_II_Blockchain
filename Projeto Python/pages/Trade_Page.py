import streamlit as st
import Controller as ctrl

ctrl.initialize_session()

pokedata = st.session_state[ctrl.SESSION_DATA]
nomes_treinadores = pokedata.keys()

def show_blockchain_log():

    log = st.session_state[ctrl.SESSION_LOG]

    count = 0
    log = log.split('\n')
    for line in log:
        st.write(f"Block #{count}")
        count += 1
        line = line[line.find("[")+1:line.find("]")]
        line = line.split(',')
        
        for log_data in line:
            st.write(log_data)
        else:
            st.write("---------")
    
    
    
    # Block #0 [previousHash : 0, timestamp : 1659589335.969274, data : Genesis Block, Nonce : 220] Block #1 [previousHash : 002d86ef185cc273cd032c184cb52e2a013b7dfc0ed94d684d111d87addea33c, timestamp : 1659589335.972266, data : <Transaction.Transaction object at 0x000002425315F2E0>, Nonce : 617]
    pass

def show_trade_form():

    id_treinador_01 = st.selectbox(label="Treinador 01", options=nomes_treinadores)
    id_pokemon = st.selectbox(label="select a Pokemon", options=pokedata[id_treinador_01].pokemons)

    nomes_sem_treinador_01 = list(filter(lambda x: x != id_treinador_01, nomes_treinadores))

    id_treinador_02 = st.selectbox(label="Treinador 02", options=nomes_sem_treinador_01)
    
    col_1, _, _, col_4 = st.columns(4)

    with col_1:
        if st.button("E N V I A R"):
            # trocar(id_treinador_01, id_treinador_02, id_pokemon)
            ctrl.trocar(id_treinador_01, id_treinador_02, id_pokemon)
    with col_4:
        if st.button("Show Log"):
            show_blockchain_log()



show_trade_form()


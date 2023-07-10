import streamlit as st

import services.database as db

import controller.paciente as paciente
import controller.funcionario as funcionario

def deletar_paciente():
    st.session_state.dele = False
    st.title('Deletar Dados')

    delete_cpf = st.text_input(label = 'Insira o cpf' )
    button_delete_select = st.button('Deletar')

    if button_delete_select:
        paciente.excluir(delete_cpf)
        st.success('Paciente deletado com sucesso!')


def deletar_funcionario():
    st.session_state.dele = False
    st.title('Deletar Dados')

    delete_cpf = st.text_input(label = 'Insira o cpf' )
    button_delete_select = st.button('Deletar')

    if button_delete_select:
        funcionario.excluir(delete_cpf)
        st.success('Funcionario deletado com sucesso!')
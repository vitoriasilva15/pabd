
import streamlit as st

import services.database as db

import page.insert as insert
import page.select as select
import page.delete as delete 

#criando a barra lateral do menu
st.sidebar.title('Clínica Sorrisos')
selectbox = st.sidebar.selectbox('Ação', ['Inserir dados (Paciente)', 'Inserir dados (Funcionário)', 'Consultar Paciente', 'Consultar Funcionário', 'Consultar dados Clínica', 'Deletar paciente', 'Deletar funcionario'])

if selectbox == 'Inserir dados (Paciente)':
    insert.inserir_paciente()

if selectbox == 'Inserir dados (Funcionário)':
    insert.inserir_funcionario()

if selectbox == 'Consultar Paciente':
    select.consultar_paciente()

if selectbox == 'Consultar Funcionário':
    select.consultar_funcionario()

if selectbox == 'Consultar dados Clínica':
    select.consultar_clinica()

if selectbox == 'Deletar paciente':
    delete.deletar_paciente()

if selectbox == 'Deletar funcionario':
    delete.deletar_funcionario()
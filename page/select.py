import streamlit as st

import services.database as db

import controller.paciente as paciente
import controller.funcionario as funcionario
import controller.clinica as clinica


def consultar():
    st.title('Consultar Dados Paciente')
    colunas = st.columns((1,2,1,2,1))
    campos = [ 'Nome', 'cpf', 'Telefone', 'Rua', 'Cidade', 'Estado''Excluir']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in cliente.selecionar():
        col1, col2, col3, col4, col5 = st.columns((1,2,1,2,1))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        button_excluir = col5.empty()
        on_click_excluir = button_excluir.button('x', 'btnExcluir' + str(item[0]))
        
        if on_click_excluir:
            continue
            #cliente.excluir(item[0])   
            
def consultar_paciente():
    st.title('Consultar Dados Paciente')
    colunas = st.columns((1,2,1,2,1,2,1))
    campos = [ 'Nome', 'cpf', 'Telefone', 'Rua', 'Cidade', 'Estado', 'Indicação']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in paciente.selecionar():
        col1, col2, col3, col4, col5, col6, col7 = st.columns((1,2,1,2,1,2,1))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])
        col6.write(item[5])
        col7.write(item[6])

def consultar_funcionario():
    st.title('Consultar Dados Funcionário')
    colunas = st.columns((1,2,1,2,1,2,1,2))
    campos = [ 'Nome', 'cpf', 'Telefone', 'Rua', 'Cidade', 'Estado', 'Salário', 'Função']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in funcionario.selecionar():
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1,2,1,2,1,2,1,2))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])
        col6.write(item[5])
        col7.write(item[6])
        col8.write(item[7])

def consultar_clinica():
    st.title('Consultar Dados Clínica')
    colunas = st.columns((1,2,1,2,1,2,))
    campos = [ 'Cnpj', 'nome', 'Telefone', 'Rua', 'Cidade', 'Estado',]
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in clinica.selecionar():
        col1, col2, col3, col4, col5, col6 = st.columns((1,2,1,2,1,2))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])
        col6.write(item[5])
    
        
            
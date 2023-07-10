import streamlit as st

import services.database as db

import controller.paciente as paciente
import controller.funcionario as funcionario

def inserir_paciente():
    st.title('Inserir Dados (paciente)')
    redes_sociais = ['Instagram', 'Twitter', 'Whatsapp']
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', ' MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF']
    with st.form(key='insert'):
        input_name = st.text_input(label='Nome: ')
        input_cpf = st.text_input(label='Cpf: ')
        input_telefone = st.text_input(label='Número de telefone: ')
        input_rua = st.text_input(label='Rua:' )
        input_cidade = st.text_input(label='Cidade:' )
        input_estado = st.selectbox(label='Estado:', options=estados )
        input_indicacao = st.selectbox(label= 'Indicação: ', options=redes_sociais)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            paciente.incluir(input_name, input_cpf, input_telefone, input_rua, input_cidade, input_estado, input_indicacao)
            st.success('Paciente incluido com sucesso')

def inserir_funcionario():
    st.title('Inserir Dados (funcionario)')
    funcoes = ['Dentista', 'Recepcionista', 'auxiliar de limpeza']
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', ' MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF']
    with st.form(key='insert'):
        input_name = st.text_input(label='Nome: ')
        input_cpf = st.text_input(label='Cpf: ')
        input_telefone = st.text_input(label='Número de telefone: ')
        input_rua = st.text_input(label='Rua:' )
        input_cidade = st.text_input(label='Cidade:' )
        input_estado = st.selectbox(label='Estado:', options=estados )
        input_salario = st.text_input(label = 'Salario')
        input_funcao = st.selectbox(label= 'funcao:' , options=funcoes)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            funcionario.incluir(input_name, input_cpf, input_telefone, input_rua, input_cidade, input_estado, input_salario, input_funcao)
            st.success('Funcionario incluido com sucesso')

#def inserir():
#   st.title('Inserir Dados')
#    profissoes = ['Analista de Dados', 'Engenheiro de Dados', 'Cientista de Dados']
#    
#    with st.form(key='insert'):
#       input_name = st.text_input(label='Insira o nome:')
#       input_cpf = st.number_input(label='Insira o cpf', format='%d', step=1)
#        input_data = st.date_input(label='Insira a data de nascimento: ')
#        input_job = st.selectbox(label='Insira a Profissão', options=profissoes)
#        
#        buttom_submit = st.form_submit_button('Enviar')
#        
#        if buttom_submit:
#            cliente.incluir(input_name, input_cpf, input_job)
#           st.success('Cliente incluido com sucesso')
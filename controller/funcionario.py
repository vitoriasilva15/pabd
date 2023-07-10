#carregando as funções em outros arquivos .py
import services.database as db
import controller.funcionario as funcionario

#função para inserir registro no banco de dados
def incluir(nome, cpf, telefone, rua, cidade, estado, salario, funcao):
    db.cur.execute("""
                   INSERT into public.tb_funcionario (nome, cpf, telefone, rua, cidade, estado, salario, funcao)
                   VALUES ('%s','%s','%s', '%s','%s','%s', '%s', '%s')
                   """ % (nome, cpf, telefone, rua, cidade, estado, salario, funcao))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tb_funcionario
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def excluir(cpf):
    db.cur.execute("""
            DELETE FROM tb_funcionario WHERE cpf = '%s' 
    """ % (cpf))
    db.con.commit()
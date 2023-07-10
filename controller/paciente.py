#carregando as funções em outros arquivos .py
import services.database as db
import controller.paciente as paciente

#função para inserir registro no banco de dados
def incluir(nome, cpf, telefone, rua, cidade, estado, indicacao):
    db.cur.execute("""
                   INSERT into public.tb_paciente (nome, cpf, telefone, rua, cidade, estado, indicacao)
                   VALUES ('%s','%s','%s', '%s','%s','%s', '%s')
                   """ % (nome, cpf, telefone, rua, cidade, estado, indicacao))
    db.con.commit()
    
# funcao para excluir registros no banco de dados
def excluir(cpf):
    db.cur.execute("""
            DELETE FROM tb_paciente WHERE cpf = '%s' 
    """ % (cpf))
    db.con.commit()





def selecionar():
    db.cur.execute("""
                   SELECT * FROM tb_paciente
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows
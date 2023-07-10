import services.database as db

def selecionar():
    db.cur.execute("""
                   SELECT * FROM tb_clinica
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

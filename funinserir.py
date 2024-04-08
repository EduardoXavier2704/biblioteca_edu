from conexao import connect

def insert(mydb, Titulo, Nomeautor, Ano, Status_):
    mycursor = mydb.cursor()

    sql = "INSERT INTO livros (Titulo, Nomeautor, Ano, Status_) VALUES (%s, %s, %s, %s)"
    val = (Titulo, Nomeautor, Ano, Status_)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()
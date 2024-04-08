from conexao import connect

def update(mydb, Titulo, Status_):
    mycursor = mydb.cursor()

    sql = "UPDATE livros SET Status_ = %s WHERE Titulo = %s"
    val = (Status_, Titulo)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Atualizado com sucesso!.")

    mycursor.close()
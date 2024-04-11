from conexao import connect

def devolver(mydb, Titulo, Status_):
    mycursor = mydb.cursor()

    sql = "UPDATE livros SET Status_ = %s WHERE Titulo = %s AND Status_ = 'Emprestado'"

    val = (Status_, Titulo)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Devolvido com sucesso!")

    mycursor.close()
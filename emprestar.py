from conexao import connect

def emprestar(mydb, Titulo, Status_):
    mycursor = mydb.cursor()

    sql = "UPDATE livros SET Status_ = %s WHERE Titulo = %s AND Status_ = 'Disponivel'"

    val = (Status_, Titulo)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Emprestado com sucesso!")

    mycursor.close()
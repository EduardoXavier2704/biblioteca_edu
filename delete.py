from conexao import connect

def delete(mydb, Titulo):
    mycursor = mydb.cursor()

    sql = "DELETE FROM livros WHERE Titulo = %s"
    val = (Titulo,)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Deletado com sucesso!.")

    mycursor.close()
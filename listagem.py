from conexao import connect

def listagem(mydb):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM livros")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mycursor.close()
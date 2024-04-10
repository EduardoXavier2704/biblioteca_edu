from conexao import connect

def login(mydb, Nome, Senha):
    mycursor = mydb.cursor()

    sql = "SELECT Nome, Senha FROM cadastros WHERE Nome = %s AND Senha = %s"
    val = (Nome, Senha)

    mycursor.execute(sql, val)

    results = mycursor.fetchall()

    if results:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha inválidos.")

    mycursor.close()
    
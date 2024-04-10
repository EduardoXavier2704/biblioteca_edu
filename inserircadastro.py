from conexao import connect
mydb = connect()

def insert(mydb, Nome, Email, Senha, cpf):
    mycursor = mydb.cursor()

    sql = "INSERT INTO cadastros (Nome, Email, Senha, cpf) VALUES (%s, %s, %s, %s)"
    val = (Nome, Email, Senha, cpf)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()
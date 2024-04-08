from conexao import connect
from funinserir import insert
from funcaoupd import update
from delete import delete
from listagem import listagem

mydb = connect()

Titulo = None
Nomeautor = None
Ano = None
Status_ = None

def escolha(mydb, Titulo, Nomeautor, Ano, Status_):
    while True:
        opcao = input("Qual das opções você deseja escolher?: (1) atualizar; (2) inserir; (3) deletar; (4) listar; (5) para sair: ")
        if opcao == '1':
            Titulo = input("Insira o título: ")
            Status_ = input("Insira o novo Status: ")
            update(mydb, Titulo, Status_)
        elif opcao == '2':
            Titulo = input("Insira o título: ")
            Nomeautor = input("Insira o Nomeautor: ")
            Ano = input("Insira o Ano: ")
            Status_ = input("Insira o Status: ")
            insert(mydb, Titulo, Nomeautor, Ano, Status_)
        elif opcao == '3':
            Titulo = input("Insira o título: ")
            delete(mydb, Titulo)
        elif opcao == '4':
            listagem(mydb)
        elif opcao == '5':
            print("Obrigado por utilizar o código!")
            exit()
        else:
            print("O seu programa deu erro!")
            exit()

escolha(mydb, Titulo, Nomeautor, Ano, Status_)
'''fetchall()'''
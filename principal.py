from conexao import connect
from funinserir import insert
from funcaoupd import update
from delete import delete
from listagem import listagem
from inserircadastro import insert as cadastro_insert
from loginbd import login as login_check
from emprestar import emprestar as emprestar_livro
from devolver import devolver as devolver_livro

mydb = connect()

def escolher_login():
    print("Bem vindo ao sistema de cadastro de livros!")
    escolha = input("Insira (1) para login e (2) para cadastro: ")

    if escolha == '1':
         Nome = input("Insira o seu nome: ")
         Senha = input("Insira a sua senha: ")
         login_check(mydb, Nome, Senha)
         escolha_opcao(mydb)
    elif escolha == "2":
        Nome = input("Insira o seu nome: ")
        Email = input("Insira o seu email: ")
        Senha = input("Insira a sua senha: ")
        cpf = input("Insira o seu CPF: ")
        cadastro_insert(mydb, Nome, Email, Senha, cpf)
        print("Cadastro realizado com sucesso! Faça login para acessar o sistema.")
        escolher_login()
    else:
        print("Opção inválida, Tente novamente!")
        escolher_login()

def escolha_opcao(mydb):
    while True:
        opcao = input("Qual das opções você deseja escolher?: (1) atualizar; (2) inserir; (3) deletar; (4) listar; (5) emprestar; (6) devolver; (7) para sair: ")
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
            Titulo = input("Insira o título: ")
            Status_ = input("Insira o novo status: ")
            emprestar_livro(mydb, Titulo, Status_)
        elif opcao == '6':
            Titulo = input("Insira o Título: ")
            Status_ = input("Insira o novo status: ")
            devolver_livro(mydb, Titulo, Status_)
        elif opcao == '7':
            print("Obrigado por utilizar o código!")
            exit()
        else:
            print("O seu programa deu erro!")
            exit()

escolher_login()
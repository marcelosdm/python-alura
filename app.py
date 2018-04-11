# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print 'Digite um nome'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print 'Listando nomes'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome você deseja remover?'
    nome = raw_input()
    nomes.remove(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite 1 para cadastrar, 2 para listar, 3 para remover, 0 para encerrar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)

menu()
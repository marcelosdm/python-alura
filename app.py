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

def alterar(nomes):
    print ('Qual nome você deseja alterar?')
    nome_alterar = raw_input()
    if(nome_alterar in nomes):
        posicao = nomes.index(nome_alterar)
        print ('Digite o novo nome:')
        nome_novo = raw_input()
        nomes[posicao] = nome_novo

def procurar(nomes):
    print ('Digite o nome a procurar:')
    nome_procurar = raw_input()
    if(nome_procurar in nomes):
        print ('Nome %s foi encontrado') % (nome_procurar)
    else:
        print ('O nome %s não foi cadastrado') % (nome_procurar)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 0 para encerrar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            procurar(nomes)

menu()
# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe para moldar perfis de usuários'
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, Empresa: %s, Telefone: %s' % (self.nome, self.empresa, self.telefone)
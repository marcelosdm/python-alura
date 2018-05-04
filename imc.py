# -*- coding: UTF-8 -*-

class Pessoa(object):
    def __init__ (self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    # def imprime(self):
    #     imc = self.peso / (self.altura ** 2)
    #     print 'IMC de %s: %s' % (self.nome, imc)

    def imprime(self):
        print 'IMC de %s: %s' % (self.nome, (self.peso / (self.altura ** 2)))
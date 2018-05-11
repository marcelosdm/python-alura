class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def calcular_imposto(self):
        imposto = self.saldo * 0.10
        return imposto

class ContaCorrente(Conta):
    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20
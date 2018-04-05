def gera_nome_convite(convidado):
    posicao_final = len(convidado)
    posicao_inicial = posicao_final -4
    parte1 = convidado[0:4]
    parte2 = convidado[posicao_inicial:posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(convidado):
    print 'Enviando convite para %s' % (convidado)

def processa_convite(convidado):
    nome_formatado = gera_nome_convite(convidado)
    envia_convite(nome_formatado)
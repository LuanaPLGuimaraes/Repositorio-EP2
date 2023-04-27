from Funcoes import *
from random import randint as sorteia 

# POSICIONANDO AMBAS FROTAS NO TABULEIRO
# 1 porta-aviao, tamanho 4
# 2 navio-tanque, tamanho 3
# 3 contratorpedeiro, tamanho 2
# 4 submarinos, tamanho 1

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
while frota['porta-aviões'] == []:
    print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')

    linha = int(input('Qual linha?'))
    coluna = int(input('Qual coluna?'))
    orientacao = input('Qual orientação?')
    if orientacao == '1':
        orientacao = 'vertical'
    if orientacao == '2':
        orientacao = 'horizontal'

    valido = posicao_valida(frota, linha, coluna, orientacao, 4)

    if valido == True:
        frota = preenche_frota(frota, 'porta-aviões', linha, coluna, orientacao, 4)

    else:
        print('Esta posição não está válida!')


while len(frota['navio-tanque']) < 2:
    print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')

    linha = int(input('Qual linha?'))
    coluna = int(input('Qual coluna?'))
    orientacao = input('Qual orientação?')
    if orientacao == '1':
        orientacao = 'vertical'
    if orientacao == '2':
        orientacao = 'horizontal'

    valido = posicao_valida(frota, linha, coluna, orientacao, 3)

    if valido == True:
        frota = preenche_frota(frota, 'navio-tanque', linha, coluna, orientacao, 3)

    else:
        print('Esta posição não está válida!')
        

while len(frota['contratorpedeiro']) < 3:
    print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')

    linha = int(input('Qual linha?'))
    coluna = int(input('Qual coluna?'))
    orientacao = input('Qual orientação?')
    if orientacao == '1':
        orientacao = 'vertical'
    if orientacao == '2':
        orientacao = 'horizontal'

    valido = posicao_valida(frota, linha, coluna, orientacao, 2)

    if valido == True:
        frota = preenche_frota(frota, 'contratorpedeiro', linha, coluna, orientacao, 2)

    else:
        print('Esta posição não está válida!')

while len(frota['submarino']) < 4:
    print('Insira as informações referentes ao navio submarino que possui tamanho 1')

    linha = int(input('Qual linha?'))
    coluna = int(input('Qual coluna?'))
    orientacao = 'horizontal'
    
    valido = posicao_valida(frota, linha, coluna, orientacao, 1)

    if valido == True:
        frota = preenche_frota(frota, 'submarino', linha, coluna, orientacao, 1)

    else:
        print('Esta posição não está válida!')


#JOGADAS DO JOGADOR

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

oponente_posicionado = posiciona_frota(frota_oponente)
jogador_posicionado = posiciona_frota(frota)

jogando = True
lista_posicoes = []
lista_posicoes_op = []

while jogando == True:
    
    tabuleiros = (monta_tabuleiros(jogador_posicionado, oponente_posicionado))
    print(tabuleiros)

    linha = int(input('Qual linha deseja atacar?'))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Qual linha deseja atacar?'))


    coluna = int(input('Qual coluna deseja atacar?'))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Qual coluna deseja atacar?'))


    lista_pos = [linha, coluna]

    while lista_pos in lista_posicoes:
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha, coluna))

        linha = int(input('Qual linha deseja atacar?'))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Qual linha deseja atacar?'))


        coluna = int(input('Qual coluna deseja atacar?'))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Qual coluna deseja atacar?'))


    lista_posicoes.append(lista_pos)


    oponente_posicionado = faz_jogada(oponente_posicionado, linha, coluna)

    verifica_venceu = afundados(frota_oponente, oponente_posicionado)

    if verifica_venceu == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    #COMO NAO VENCEU: JOGADA OPONENTE

    linha_op = sorteia(0,9)
    coluna_op = sorteia(0,9)

    lista_pos_op = [linha_op, coluna_op]

    while lista_pos_op in lista_posicoes_op:
        linha_op = sorteia(0,9)
        coluna_op = sorteia(0,9)


    lista_posicoes_op.append(lista_pos_op)

    print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_op,coluna_op))

    jogador_posicionado = faz_jogada(jogador_posicionado, linha_op, coluna_op)

    verifica_venceu_op = afundados(frota, jogador_posicionado)

    if verifica_venceu_op == 10:
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False
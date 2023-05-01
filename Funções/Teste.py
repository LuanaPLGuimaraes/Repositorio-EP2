from Funcoes import *
from random import randint as sorteia 

# POSICIONANDO AMBAS FROTAS
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


# DEFININDO TABULEIROS CONFORME FROTAS
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


tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
ataques_jogador = []
ataques_oponente = []

jogando = True

while jogando:

    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

# ATAQUE JOGADOR

    # validando entradas
    ataque_linha = int(input('Qual linha deseja atacar?'))
    while ataque_linha > 9 or ataque_linha < 0:
        print('Linha inválida!')
        ataque_linha = int(input('Qual linha deseja atacar?'))

    ataque_coluna = int(input('Qual coluna deseja atacar?'))
    while ataque_coluna > 9 or ataque_coluna < 0:
        print('Coluna inválida!')
        ataque_coluna = int(input('Qual coluna deseja atacar?'))


    while [ataque_linha, ataque_coluna] in ataques_jogador:

        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(ataque_linha, ataque_coluna) )

        ataque_linha = int(input('Qual linha deseja atacar?'))
        while ataque_linha > 9 or ataque_linha < 0:
            print('Linha inválida!')
            ataque_linha = int(input('Qual linha deseja atacar?'))

        ataque_coluna = int(input('Qual coluna deseja atacar?'))
        while ataque_coluna > 9 or ataque_coluna < 0:
            print('Coluna inválida!')
            ataque_coluna = int(input('Qual coluna deseja atacar?'))

    #atualizando tabuleiro
    ataques_jogador.append([ataque_linha, ataque_coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, ataque_linha, ataque_coluna)

    #verificando se venceu

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False


    #COMO NAO VENCEU: JOGADA OPONENTE
    else:
        linha_op = sorteia(0,9)
        coluna_op = sorteia(0,9)

        while [linha_op, coluna_op] in ataques_oponente:
            linha_op = sorteia(0,9)
            coluna_op = sorteia(0,9)

        ataques_oponente.append([linha_op, coluna_op])

        print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_op, coluna_op))

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_op, coluna_op)

        if afundados(frota, tabuleiro_jogador) == 10:

            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
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

while jogando == True:
    
    tabuleiros = (monta_tabuleiros(jogador_posicionado, oponente_posicionado))
    print(tabuleiros)

    lista_linhas = []
    lista_colunas = []

    linha = int(input('Qual linha deseja atacar?'))
    if linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Qual linha deseja atacar?'))


    coluna = int(input('Qual coluna deseja atacar?'))
    if coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Qual coluna deseja atacar?'))

    if linha in lista_linhas and coluna in lista_colunas:
        print('A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')

    else:
        lista_linhas.append(linha)
        lista_colunas.append(coluna)

        novo_tabuleiro_oponente = faz_jogada(oponente_posicionado, linha, coluna)

        verifica_venceu = afundados(frota_oponente, novo_tabuleiro_oponente)

        if verifica_venceu == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False

        #COMO NAO VENCEU: JOGADA OPONENTE
        else:
            lista_linhas_op = []
            lista_colunas_op = []

            linha_op = sorteia(0,9)
            coluna_op = sorteia(0,9)
        
            if linha_op in lista_linhas_op and coluna_op in lista_colunas_op:
                linha_op = sorteia(0,9)
                coluna_op = sorteia(0,9)

            else:
                lista_linhas_op.append(linha_op)
                lista_colunas_op.append(coluna_op)

                print('Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}')

                novo_tabuleiro_jogador = faz_jogada(jogador_posicionado, linha_op, coluna_op)

                verifica_venceu_op = afundados(frota, novo_tabuleiro_jogador)

                if verifica_venceu_op == 10:
                    print('Xi! O oponente derrubou toda a sua frota =(')
                    jogando = False
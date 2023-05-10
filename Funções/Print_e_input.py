from Funcoes import *
from random import randint as sorteia 

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
    }
tamanho_navios = [4,3,2,1]
for i, navio in enumerate(frota):
    orientacao = 'horizontal'
    while len(frota[navio])<tamanho_navios[-i+1]:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,tamanho_navios[i]))
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = input('Orientação: [1] Vertical [2] Horizontal ')
        if orientacao == '1':
            orientacao = 'vertical'
        valido = posicao_valida(frota, linha, coluna, orientacao, tamanho_navios[i])
        if valido:
            frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho_navios[i])
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

while jogando:
    
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


    # lista_pos = [linha, coluna]

    while [linha, coluna] in lista_posicoes:
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha, coluna))

        linha = int(input('Qual linha deseja atacar?'))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Qual linha deseja atacar?'))

        coluna = int(input('Qual coluna deseja atacar?'))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Qual coluna deseja atacar?'))

    #lista_pos = [linha, coluna]
    lista_posicoes.append([linha, coluna])

    oponente_posicionado = faz_jogada(oponente_posicionado, linha, coluna)

    verifica_venceu = afundados(frota_oponente, oponente_posicionado)

    if verifica_venceu == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    #COMO NAO VENCEU: JOGADA OPONENTE
    else:
        linha_op = sorteia(0,9)
        coluna_op = sorteia(0,9)

        while [linha_op, coluna_op] in lista_posicoes_op:
            linha_op = sorteia(0,9)
            coluna_op = sorteia(0,9)
            
            lista_pos_op = [linha_op, coluna_op]

        lista_posicoes_op.append([linha_op, coluna_op])

        print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_op,coluna_op))

        jogador_posicionado = faz_jogada(jogador_posicionado, linha_op, coluna_op)

        verifica_venceu_op = afundados(frota, jogador_posicionado)

        if verifica_venceu_op == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
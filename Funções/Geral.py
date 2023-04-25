#Exercicio definindo posicoes
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao=[]
    for i in range(tamanho):
        if orientacao=='vertical':
            posicao.append([linha, coluna])
            linha+=1
        elif orientacao=='horizontal':
            posicao.append([linha, coluna])
            coluna+=1
    return posicao

#Exercicio preenchendo frota com base no definindo posicoes
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao= define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota.keys():
        frota[nome_navio].append(posicao)

    else:
        frota[nome_navio] = [posicao]
    return frota

#Exercicio Faz jogada 
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

#Exercicio Posiciona Frota
def posiciona_frota(posicoes):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

    for navios in posicoes.values():
        for i in range(len(navios)):
            for j in range(len(navios[i])):
                tabuleiro[navios[i][j][0]][navios[i][j][1]] = 1

    return tabuleiro 

#Exercício Quantas embarcações afundadas?
def afundados(frota, tabuleiro):
    quantidade_afundados=0
    for l_posicoes in frota.values():
        for i in range(len(l_posicoes)):
            contador_tamanho=0
            for j in range(len(l_posicoes[i])):
                linhazinha=l_posicoes[i][j][0]
                colunazinha=l_posicoes[i][j][1]
                if tabuleiro[linhazinha][colunazinha]=="X":
                    contador_tamanho+=1
                if contador_tamanho==len(l_posicoes[i]):
                    quantidade_afundados+=1  
                print(contador_tamanho)
    print(quantidade_afundados)
    return quantidade_afundados

#Exercicio posicao valida
def posicao_valida(posicionados, linha, coluna, orientacao, tamanho):
    novo = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in novo:
        if posicao[0] > 9 or posicao[1] > 9:
            return False
        else:
            for ocupados in posicionados.values():
                for i in ocupados:
                    for j in i:
                        if posicao[0] == j[0] and posicao[1] == j[1]:
                            return False
                        
    return True



# Exercicio posicionando frota
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

#Exercício Jogadas do jogador

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

jogando = True

while jogando == True:

    tabuleiro_jogador=posiciona_frota(frota) #posicionando as frotas do jogador
    tabuleiro_oponente=posiciona_frota(frota_oponente) #posicionando as frotas do oponente

    #montando o tabuleiro do jogo
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    
    lista_linha=[]
    lista_coluna=[]

    linha_ataque = int(input('Qual linha deseja atacar?'))

    if linha_ataque < 0 or linha_ataque > 9: #confere se a linha é válida
        print('Linha inválida!')
        linha_ataque = int(input('Qual linha deseja atacar?'))

    coluna_ataque = int(input('Qual coluna deseja atacar?'))

    if coluna_ataque < 0 or coluna_ataque > 9: #confere se a coluna é válida
        print('Coluna inválida!')
        coluna_ataque = int(input('Qual coluna deseja atacar?'))

    for i in range(len(lista_coluna)): #jogando 
        if lista_coluna[i] == coluna_ataque and lista_linha[i] == linha_ataque:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_ataque, coluna_ataque))
            
    lista_coluna.append(coluna_ataque)
    lista_linha.append(linha_ataque)

    novo_tabuleiro_oponente=faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

    verifica_se_venceu=afundados(frota_oponente, novo_tabuleiro_oponente)
    
    if verifica_se_venceu == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando=False
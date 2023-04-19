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

#Exercicio faz jogada 
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
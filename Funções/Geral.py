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
def posiciona_frota(informacoes_navios):
    posicoes = preenche_frota(informacoes_navios)


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

#Exercicio posicao valida
def posicao_valida(ja_posicionados, linha, coluna, orientacao, tamanho):
    deseja = define_posicoes(linha, coluna, orientacao, tamanho)
    valor = False

    for posicoes in ja_posicionados.values():
        for i in range(len(posicoes)):
            for j in range(len(posicoes[i])):
                for k in range(len(deseja)):
                    if deseja[k][0] == posicoes[i][j][0] and deseja[k][1] == posicoes[i][j][1]:
                        return False
                    else:
                        valor = True

    return valor
                

print(posicao_valida({
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}, 1,5,'horizontal',4))

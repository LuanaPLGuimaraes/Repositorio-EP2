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

print(frota)
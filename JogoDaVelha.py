import random

#define o tabuleiro e coloca seus espaços como vazios
tabuleiro = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

#imprime o tabuleiro conforme suas posições que serão preenchidas ao longo do jogo
def imprimirTabuleiro(tabuleiro):
    print('+---+---+---+')
    print('| ' + tabuleiro[1] + ' | ' + tabuleiro[2] + ' | ' + tabuleiro[3] +' |')
    print('+---+---+---+')
    print('| ' + tabuleiro[4] + ' | ' + tabuleiro[5] + ' | ' + tabuleiro[6] +' |')
    print('+---+---+---+')
    print('| ' + tabuleiro[7] + ' | ' + tabuleiro[8] + ' | ' + tabuleiro[9] +' |')
    print('+---+---+---+')
    print("\n")

#verifica se um espaço está livre no tabuleiro
def espacoLivre(posicao):
    if tabuleiro[posicao] == ' ':
        return True
    else:
        return False

#insere a jogada do jogador ou da ia no tabuleiro.
#verifica se houve um ganhador ou se deu velha

def inserirJogada(letra, posicao, escolha):
    if espacoLivre(posicao):
        tabuleiro[posicao] = letra
        imprimirTabuleiro(tabuleiro)
        if checarVencedor():
            if letra != escolha:
                print("IA ganhou, tente outra vez.")
                exit()
            else:
                print("Você ganhou!!")
                exit()
        if (checarVelha()):
            print("Deu velha!")
            exit()

        return


    else:
        print("Espaço ocupado")
        posicao = int(input("Tente outra posição:  "))
        inserirJogada(letra, posicao, escolha)
        return


#verifica todas as possibilidades de ser um vencedor
def checarVencedor():
    if (tabuleiro[1] == tabuleiro[2] and tabuleiro[1] == tabuleiro[3] and tabuleiro[1] != ' '):
        return True
    elif (tabuleiro[4] == tabuleiro[5] and tabuleiro[4] == tabuleiro[6] and tabuleiro[4] != ' '):
        return True
    elif (tabuleiro[7] == tabuleiro[8] and tabuleiro[7] == tabuleiro[9] and tabuleiro[7] != ' '):
        return True
    elif (tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] != ' '):
        return True
    elif (tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[2] != ' '):
        return True
    elif (tabuleiro[3] == tabuleiro[6] and tabuleiro[3] == tabuleiro[9] and tabuleiro[3] != ' '):
        return True
    elif (tabuleiro[1] == tabuleiro[5] and tabuleiro[1] == tabuleiro[9] and tabuleiro[1] != ' '):
        return True
    elif (tabuleiro[7] == tabuleiro[5] and tabuleiro[7] == tabuleiro[3] and tabuleiro[7] != ' '):
        return True
    else:
        return False

#marca o espaço ganhador a fim da ia tomar as suas decisões baseadas nessas combinações de ganho
def checaEspacoGanhador(marca):
    if tabuleiro[1] == tabuleiro[2] and tabuleiro[1] == tabuleiro[3] and tabuleiro[1] == marca:
        return True
    elif (tabuleiro[4] == tabuleiro[5] and tabuleiro[4] == tabuleiro[6] and tabuleiro[4] == marca):
        return True
    elif (tabuleiro[7] == tabuleiro[8] and tabuleiro[7] == tabuleiro[9] and tabuleiro[7] == marca):
        return True
    elif (tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] == marca):
        return True
    elif (tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[2] == marca):
        return True
    elif (tabuleiro[3] == tabuleiro[6] and tabuleiro[3] == tabuleiro[9] and tabuleiro[3] == marca):
        return True
    elif (tabuleiro[1] == tabuleiro[5] and tabuleiro[1] == tabuleiro[9] and tabuleiro[1] == marca):
        return True
    elif (tabuleiro[7] == tabuleiro[5] and tabuleiro[7] == tabuleiro[3] and tabuleiro[7] == marca):
        return True
    else:
        return False

#verifica se todos os espaços foram preenchidos. Caso não haja vencedor, será uma velha.
def checarVelha():
    for lugar in tabuleiro.keys():
        if (tabuleiro[lugar] == ' '):
            return False
    return True

#chama a jogada do humano e a insere no tabuleiro caso seja um espaço livre
def jogadaHumano(humano, escolha):
    escolhadaposicao= False
    while not escolhadaposicao:
        posicao = int(input("Entre com a posição para " + escolha + " : "))
        if (posicao>0 and posicao<10):
            inserirJogada(humano, posicao, escolha)
            escolhadaposicao=True
            return
        else:
            print("Posicao inválida, tente novamente!")

#define a jogada da ia
def jogadaComputador(humano, ia, escolha):
    melhorPontuacao = -800  #inicia a melhor pontuação em um número baixo
    melhorMovimento = 0 #inicia o melhor movimento zerado
    for lugar in tabuleiro.keys(): #para cada espaço no tabuleiro
        if (tabuleiro[lugar] == ' '): #verifica se é vazio
            tabuleiro[lugar] = ia #o espaço vazio vai receber a 'O' ou 'X' de acordo com a ia
            pontuacao = minimax(tabuleiro, False, humano, ia) #chama o minimax para ver a pontuação

            tabuleiro[lugar] = ' '
            if (pontuacao > melhorPontuacao):
                melhorPontuacao = pontuacao
                melhorMovimento = lugar

    inserirJogada(ia, melhorMovimento, escolha)
    return

#função minimax
def minimax(tabuleiro, estaMaximizado, humano, ia):
    if (checaEspacoGanhador(ia)): #chama função espaço ganhador. Com todas as possibilidades preenchidas, ele verifica se uma delas há a possibilidade de ganhar.
        return 100 #retorna um valor 100
    elif (checaEspacoGanhador(humano)): #chama função espaço ganhador. Com todas as possibilidades preenchidas, ele verifica se uma delas há a possibilidade do humano ganhar/
        return -100 #retorna -100
    elif (checarVelha()): #chama função espaço ganhador. Caso a jogada resulte em velha
        return 0  #retorna 0
    #recursiva do minimax
    if (estaMaximizado): 
        melhorPontuacao = -800
        for lugar in tabuleiro.keys():
            if (tabuleiro[lugar] == ' '):
                    tabuleiro[lugar] = ia
                    pontuacao = minimax(tabuleiro, False, humano, ia)
                    tabuleiro[lugar] = ' '
                    if (pontuacao > melhorPontuacao):
                        melhorPontuacao = pontuacao
        return melhorPontuacao

    else:
        melhorPontuacao = 800
        for lugar in tabuleiro.keys():
            if (tabuleiro[lugar] == ' '):
                    tabuleiro[lugar] = humano
                    pontuacao = minimax(tabuleiro, True, humano, ia)
                    tabuleiro[lugar] = ' '
                    if (pontuacao < melhorPontuacao):
                        melhorPontuacao = pontuacao
        return melhorPontuacao

def jogadaRandomica(ia, escolha):
    vet = []
    for lugar in tabuleiro.keys():
        if(tabuleiro[lugar]==' '):
            vet.append(lugar)
    r = random.choice(vet)
    inserirJogada(ia, r, escolha)
    return

     

def main():

    primeiro = ''
    escolhadaforma = False
    escolhadoprimeiro = False
    profescolhida = False

    while not escolhadoprimeiro:
        primeiro = input("Gostaria de começar? [S/N] ").upper()
        if (primeiro == 'S' or primeiro == 'N'):
            escolhadoprimeiro=True
        else:
            print("Opção inválida, tente novamente!")

    while not escolhadaforma:
        escolha = input("Escolha O ou X: "). upper()
        if(escolha == 'X'):
            humano = 'X'
            ia = 'O'
            escolhadaforma=True
        else:
            if(escolha == 'O'):
                humano = 'O'
                ia = 'X'
                escolhadaforma=True
            else:
                print("Opção inválida, escolha novamente!")

    while not profescolhida:
        profundidade = int(input("Digite o número da dificuldade do jogo[0-9]: "))
        if(profundidade>=0 and profundidade<10):
            profescolhida=True
        else:
            print("Opção inválida, escolha novamente!")
            
    print("\n")
    print("As jogadas seguem as seguintes posições de 1-9:")
    print("\n")
    print('+---+---+---+')
    print('| ' + '1' + ' | ' + '2' + ' | ' + '3' +' |')
    print('+---+---+---+')
    print('| ' + '4' + ' | ' + '5' + ' | ' + '6' +' |')
    print('+---+---+---+')
    print('| ' + '7' + ' | ' + '8' + ' | ' + '9' +' |')
    print('+---+---+---+')
    print("\n")
    print("Boa sorte!!")
    print("\n")

    while not checarVencedor():
        if(primeiro == 'S'):
            if(int(profundidade)<=0):
                jogadaHumano(humano, escolha)
                jogadaRandomica(ia, escolha)
            else:
                jogadaHumano(humano, escolha)
                profundidade=profundidade-1
                jogadaComputador(humano, ia, escolha)
                profundidade=profundidade-1

        if(primeiro == 'N'):
            if(profundidade<=0):
                jogadaRandomica(ia, escolha)
                jogadaHumano(humano, escolha)
            else:
                jogadaComputador(humano, ia, escolha)
                profundidade=profundidade-1
                jogadaHumano(humano, escolha)
                profundidade=profundidade-1

if __name__ == "__main__":
    main()
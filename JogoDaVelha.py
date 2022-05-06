import random

tabuleiro = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

def imprimirTabuleiro(tabuleiro):
    print(tabuleiro[1] + '|' + tabuleiro[2] + '|' + tabuleiro[3])
    print('-+-+-')
    print(tabuleiro[4] + '|' + tabuleiro[5] + '|' + tabuleiro[6])
    print('-+-+-')
    print(tabuleiro[7] + '|' + tabuleiro[8] + '|' + tabuleiro[9])
    print("\n")


def espacoLivre(posicao):
    if tabuleiro[posicao] == ' ':
        return True
    else:
        return False


def inserirJogada(letra, posicao, escolha):
    if espacoLivre(posicao):
        tabuleiro[posicao] = letra
        imprimirTabuleiro(tabuleiro)
        if (checarVelha()):
            print("Deu velha!")
            exit()
        if checarVencedor():
            if letra != escolha:
                print("IA ganhou, tente outra vez.")
                exit()
            else:
                print("Você ganhou!!")
                exit()

        return


    else:
        print("Espaço ocupado")
        posicao = int(input("Tente outra posição:  "))
        inserirJogada(letra, posicao, escolha)
        return


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


def checarVelha():
    for lugar in tabuleiro.keys():
        if (tabuleiro[lugar] == ' '):
            return False
    return True


def jogadaHumano(humano, escolha):
    posicao = int(input("Enter the posicao for " + escolha + ":"))
    inserirJogada(humano, posicao, escolha)
    return


def jogadaComputador(humano, ia, escolha):
    melhorPontuacao = -800
    melhorMovimento = 0
    for lugar in tabuleiro.keys():
        if (tabuleiro[lugar] == ' '):
            tabuleiro[lugar] = ia
            pontuacao = minimax(tabuleiro, False, humano, ia)

            tabuleiro[lugar] = ' '
            if (pontuacao > melhorPontuacao):
                melhorPontuacao = pontuacao
                melhorMovimento = lugar

    inserirJogada(ia, melhorMovimento, escolha)
    return


def minimax(tabuleiro, estaMaximizado, humano, ia):
    if (checaEspacoGanhador(ia)):
        return 100
    elif (checaEspacoGanhador(humano)):
        return -100
    elif (checarVelha()):
        return 0
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
    imprimirTabuleiro(tabuleiro)
    primeiro = ''
    primeiro = input("Gostaria de começar? [S/N] ").upper()
    escolha = input("Escolha O ou X: "). upper()
    profescolhida = int(input("Digite a dificuldade do jogo[1-9]: "))
    if(escolha == 'X'):
        humano = 'X'
        ia = 'O'
    else:
        humano = 'O'
        ia = 'X'
    profescolhida = int(input("Digite a dificuldade do jogo[1-9]: "))
    while not checarVencedor():
        if(primeiro == 'S'):
            if(profescolhida<=0):
                jogadaHumano(humano, escolha)
                jogadaRandomica(ia, escolha)
            else:
                jogadaHumano(humano, escolha)
                profescolhida=profescolhida-1
                jogadaComputador(humano, ia, escolha)
                profescolhida=profescolhida-1
                print(profescolhida)

        if(primeiro == 'N'):
            if(profescolhida<=0):
                jogadaRandomica(ia, escolha)
                jogadaHumano(humano, escolha)
            else:
                jogadaComputador(humano, ia, escolha)
                profescolhida=profescolhida-1
                jogadaHumano(humano, escolha)
                profescolhida=profescolhida-1
                print(profescolhida)

if __name__ == "__main__":
    main()
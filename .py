import random

def jogar():

    print("*********************************")
    print("bem vindo ao jogo de adivinhação!")
    print("*********************************")

    Numero_secreto = random. randrange (1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print(" (1) Fácil (2) Médio (3) Dificil")

    Nivel = int(input("Defina o Nivel: "))

    if(Nivel == 1):
        total_de_tentativas = 20
    elif(Nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("digite um número entre 1 e 100!")
        print("você digitou " , chute_str)
        chute = int (chute_str)

        if(chute < 1 or chute > 100):
            print("você deve digitar um numero enter 1 e 100!")
            continue

        acertou = chute == Numero_secreto  
        maior = chute > Numero_secreto
        menor = chute < Numero_secreto

        if(acertou) :
            print("você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("você chutou alto demais")
            elif(menor):
                print("você chutou baixo demais")
            pontos_perdidos = abs(Numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim Do Jogo")

if(__name__=="__main__"):
    jogar()

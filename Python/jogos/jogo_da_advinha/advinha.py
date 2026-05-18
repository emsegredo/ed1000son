from random import randint
from time import sleep

comp = randint(1, 6)
acertou = True
print("O computador gerou um número entre 1 - 6!")
jogador = int(input("Qual é o número : "))

while acertou:
    acertou = False
    tenta = 3
    while jogador != comp:
        while tenta > 0:
            sleep(3)
            tenta -= 1
            if jogador > comp:
                print("Você errou, foi um número menor")
                print(f'Você tem {tenta} tentativa(s).\n')
                jogador = int(input("Qual é o número : "))
            if jogador < comp:
                print("\nVocê errou, foi um número maior")
                print(f'Você tem {tenta} tentativa(s).\n')
                jogador = int(input("Qual é o número : "))
            if jogador == comp:
                print("\nParabéns, você acertou foi o número {}...". format(comp))
                acertou = True
                break
            if tenta == 0:
                print("\nVocê excedeu as tentativas todas!")
                break
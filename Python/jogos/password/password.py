import random
number = 1
while number != 0:
    if number == 0:
        break
    nome = input("Digite o seu nome : ")
    password = random.randint(100000, 999999)
    senha = password
    print(f'Bem-vindo, {nome}. A sua senha é : {senha}')
    if nome == "STOP":
        number = 0
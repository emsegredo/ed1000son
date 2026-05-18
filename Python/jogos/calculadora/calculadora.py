from time import sleep
while True:
    print("+" + "-" * 24 + "+")
    print("|" + " " * 6 + "Calculadora " + " " * 6 + "|")
    print("+" + "-" * 24 + "+")
    print("|" + " 1 " + "|" + " " * 2 + "Multiplicacao" + " " * 5 + "|")
    print("+" + "-" * 24 + "+")
    print("|" + " 2 " + "|" + " " * 2 + "Divisao" + " " * 11 + "|")
    print("+" + "-" * 24 + "+")
    print("|" + " 3 " + "|" + " " * 2 + "Adicao" + " " * 12 + "|")
    print("+" + "-" * 24 + "+")
    print("|" + " 4 " + "|" + " " * 2 + "Subtracao" + " " * 9 + "|")
    print("+" + "-" * 24 + "+")
    print("|" + " 5 " + "|" + " " * 2 + "Raiz Quadrada" + " " * 5 + "|")
    print("+" + "-" * 24 + "+")
    print("|" + " 0 " + "|" + " " * 2 + "Sair" + " " * 14 + "|")
    print("+" + "-" * 24 + "+")
    sleep(2)
    op = int(input("\nEscolha uma das opcoes acima : "))
    while op > 5 or op < 0:
        print("Numero invalido")
        op = int(input("\nEscolha uma das opcoes acima : "))
        sleep(1)
    if op == 1:
        print("\nVocê escolheu multiplicacao! Agora podes multiplicar dois numeros.")
        sleep(1)
        numb1 = int(input("Digite o primeiro numero : "))
        numb2 = int(input("Digite o segundo numero : "))
        sleep(1)
        print(f'{numb1} x {numb2} = {numb1*numb2}')
        sleep(1)
        while op == 1:
            tenta = int(input("\nQuer continuar?  [1] - Sim   [2] - Não : "))
            if tenta == 1:
                numb1 = int(input("Digite o primeiro numero : "))
                numb2 = int(input("Digite o segundo numero : "))
                sleep(1)
                print(f'{numb1} x {numb2} = {numb1*numb2}')
                sleep(1)
            else:
                print("\nObrigado")
                sleep(1)
                break
    if op == 2:
        print("\nVocê escolheu Divisao! Agora podes dividir dois numeros.")
        sleep(1)
        numb1 = int(input("Digite o primeiro numero : "))
        numb2 = int(input("Digite o segundo numero : "))
        sleep(1)
        print(f'{numb1} / {numb2} = {numb1/numb2}')
        sleep(1)
        while op == 2:
            tenta = int(input("\nQuer continuar?  [1] - Sim   [2] - Não : "))
            if tenta == 1:
                numb1 = int(input("Digite o primeiro numero : "))
                numb2 = int(input("Digite o segundo numero : "))
                sleep(1)
                print(f'{numb1} / {numb2} = {numb1/numb2}')
                sleep(1)
            else:
                print("\nObrigado")
                sleep(1)
                break
    if op == 3:
        print("\nVocê escolheu Adicao! Agora podes somar dois numeros.")
        sleep(1)
        numb1 = int(input("Digite o primeiro numero : "))
        numb2 = int(input("Digite o segundo numero : "))
        sleep(1)
        print(f'{numb1} + {numb2} = {numb1+numb2}')
        sleep(1)
        while op == 3:
            tenta = int(input("\nQuer continuar?  [1] - Sim   [2] - Não : "))
            if tenta == 1:
                numb1 = int(input("Digite o primeiro numero : "))
                numb2 = int(input("Digite o segundo numero : "))
                sleep(1)
                print(f'{numb1} + {numb2} = {numb1+numb2}')
                sleep(1)
            else:
                print("\nObrigado")
                sleep(1)
                break
    if op == 4:
        print("\nVocê escolheu Subtracao! Agora podes subtrair dois numeros.")
        sleep(1)
        numb1 = int(input("Digite o primeiro numero : "))
        numb2 = int(input("Digite o segundo numero : "))
        sleep(1)
        print(f'{numb1} - {numb2} = {numb1-numb2}')
        sleep(1)
        while op == 4:
            tenta = int(input("\nQuer continuar?  [1] - Sim   [2] - Não : "))
            if tenta == 1:
                numb1 = int(input("Digite o primeiro numero : "))
                numb2 = int(input("Digite o segundo numero : "))
                sleep(1)
                print(f'{numb1} - {numb2} = {numb1-numb2}')
                sleep(1)
            else:
                print("\nObrigado")
                sleep(1)
                break
    if op == 0:
        print("\nObrigado")
        sleep(1)
        print("Saindo do programa...")
        sleep(3)
        break
        
    if op == 5:
        print("\nVocê escolheu Raiz Quadrada! Agora podes saber a raiz quadra de um numero.")
        sleep(1)
        numb1 = int(input("Digite o numero : "))
        sleep(1)
        print(f'A raiz quadrada de {numb1} é : {numb1 ** 2}')
        sleep(1)
        while op == 5:
            tenta = int(input("\nQuer continuar?  [1] - Sim   [2] - Não : "))
            if tenta == 1:
                numb1 = int(input("Digite o numero : "))
                sleep(1)
                print(f'A raiz quadrada de {numb1} é : {numb1 ** 2}')
                sleep(1)
            else:
                print("\nObrigado")
                sleep(1)
                break
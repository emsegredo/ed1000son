numb = int(input("Digite um número: "))
soma = 1
if numb >= 0 and numb <= 1:
    print(f'{numb}! = 1')

elif numb < 0:
    print("Não existe factorial de números negativos!")

else:
    print(f'{numb}!', end=" = ")
    while numb >= 1:
        print(numb, end=" x ")
        soma *= numb
        numb -= 1
        if numb == 1:
            print("1 =", end=" ")
            break
    print(soma)
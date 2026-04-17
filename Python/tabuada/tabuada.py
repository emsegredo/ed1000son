print("Digite qualquer número inteiro, excepto '0'")

numb = int(input("Digite um número: "))

cont = 1
while cont < 13:
    print(f'{numb} x {cont:2} = {numb * cont:2}')
    cont += 1

else:
    if numb == 0:
        print("Só números maiores que 0")

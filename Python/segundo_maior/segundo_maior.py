from random import randint

lista = []


elementos = int(input("Digite o número de elementos da lista : "))

for i in range(elementos):
    num_al = randint(1, 100)
    lista.append(num_al)

print(lista)
lista.sort()
print(f'O segundo maior número : {lista[-2]}')
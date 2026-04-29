lista = [2, 13, -7, 23, 100, 28, 3]
new = []

for i in range(len(lista)):
    if lista[i] > 5:
        new.append(lista[i] + 2)
print(lista)
print(new)
lista = [2, 8, 9, 48, 8, 22, -12, 2]
new = set()

for i in range(len(lista)):
    if lista[i] > 5:
        new.add(lista[i] + 2)

print(lista)
print(new)
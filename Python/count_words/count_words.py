palavras = input("Digite qualquer coisa: ")

cont = 1

for i in range(len(palavras)):
    if palavras[i] == ' ' or palavras[i] == '\n' or palavras[i] == '\t':
        cont += 1
if palavras == ' ':
    cont = cont - 1
if cont > 1:
    print(f'Foram encontradas {cont} palavras!')
else:
    print(f'Foi encontrada {cont} palavra!')

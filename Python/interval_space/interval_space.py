nome = input("Digite qualquer coisa: ")
i = 0
while i <= (len(nome)-1):
    print(nome[i], end="")
    i += 1
    if i > (len(nome)-1):
        break
    print("   ", end="")
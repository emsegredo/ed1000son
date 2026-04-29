texto = input("Give a text : ")

up_low = ""

for letras in texto:
    if letras.isupper():
        up_low += letras.lower()
    else:
        up_low += letras.upper()

print(up_low)
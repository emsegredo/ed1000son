import time
n = 0
i = 0

print(f'Table of {n} :', end=" ") #Primeira impressão...

while True:
    print(f'{n * i}', end=" ")
    #time.sleep(1)
    i += 1
    if i > 10:
        n += 1
        i = 0
        if n > 10:
            break
        print(f'\nTable of {n} :', end=" ") #Imprime toda vez que i for maior que 10...

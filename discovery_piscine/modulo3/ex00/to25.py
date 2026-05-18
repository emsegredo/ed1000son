numb = int(input("Enter a number less then 25: "))

while numb < 26:
    print(f'Inside the loop, my variable is {numb}')
    if numb == 25:
        break
    numb += 1
    
else:
    print(f'Error')
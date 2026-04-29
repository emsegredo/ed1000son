number = int(input("Enter a number less than 25 : "))

if number > 25:
    print("Error.\n")
else:
    for i in range(number, 26):
        print(f'Inside the loop, my variable is {i:2}')
"""
if number > 25:
    print("Error.\n")
else:
    while number < 26:
        print(f'Inside the loop, my variable is {number:2}')
        number += 1
"""
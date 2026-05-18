"""for i in range(11):
    print(f'\nTable of {i}:', end = " ")
    for j in range(11):
        print(f'{i * j}', end = " ")"""

i = 0
j = 0

while i < 11:
    print(f'\nTable of {i}: ', end = "")
    while j < 11:
        print(f'{i * j}', end = " ")
        j += 1
    i += 1
    if j == 11:
        j = 0
        
"""nome = input("Digite qualquer coisa: ")
i = 0
while i <= (len(nome)-1):
    print(nome[i], end="")
    i += 1
    if i > (len(nome)-1):
        break
    print("   ", end="")"""

import sys

i = 0
 
if sys.argv == 2 and sys.argv[1][i] != NULL: 
    while sys.argv[1][i + 1]:
        print(sys.argv[1][i])
        print("   ")
        i += 1
print(sys.argv[1][i])
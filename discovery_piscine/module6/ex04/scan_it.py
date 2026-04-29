import sys

cont = 0

num_of_param = len(sys.argv) - 1
if num_of_param == 2:
    outro = sys.argv[2].split()
    for i in outro:
        if i == sys.argv[1]:
            cont += 1
    if cont == 0:
        print("none")
    else:
        print(cont)

else:
    #num_of_param != 2:
    print("none")
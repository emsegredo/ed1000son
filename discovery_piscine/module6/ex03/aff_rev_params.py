import sys

num_of_param = len(sys.argv) - 1
i = -1

if num_of_param < 2:
    print("none\n")

else:
    while num_of_param >= 1:
        print(f'{sys.argv[i]}')
        num_of_param -= 1
        i -= 1

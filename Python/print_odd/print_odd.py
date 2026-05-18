import sys

num_of_param = len(sys.argv) - 1
#count = 0

if num_of_param == 1:
    for count in range(len(sys.argv[1])):
        if count % 2 == 1:
            print(f'{sys.argv[1][count]}', end="")
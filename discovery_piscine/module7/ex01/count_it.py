import sys
from time import sleep

num_of_param = len(sys.argv) - 1

while num_of_param > 0:
    print(f'\nparameters: {num_of_param}')

    for i in range(1, num_of_param + 1):
        print(f'{sys.argv[i]}: {len(sys.argv[i])}')
        num_of_param -= 1

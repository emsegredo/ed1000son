import sys

num_of_param = len(sys.argv) - 1

if num_of_param == 1:
    print(sys.argv[1].lower())
else:
    print("none\n")
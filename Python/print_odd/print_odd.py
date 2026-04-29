string_ = input("Digite algo: ")

for i in range(len(string_)):
    if i % 2 == 1:
        print(string_[i], end="")
    i += 1
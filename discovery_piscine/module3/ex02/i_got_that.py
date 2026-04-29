nome = input("What you gotta say? : ")
if nome == "STOP":
    print("\n")
else:
    while True:
        nome = input("I got that! Anything else? : ")
        if nome == "STOP":
            break
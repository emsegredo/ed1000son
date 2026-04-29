from time import sleep
print("Cronómetro Feito Por Edmilson Segredo")
H = int(input("Hora: "))
M = int(input("Minuto: "))
S = int(input("Segundo: "))

if H < -1 or H > 23:
    print("O padrão da 'hora' é de 0 a 23")
    sleep(1)
    per = int(input("\nQuer tentar novamente?\n [1] - Sim\n [2] - Não\n\n"))
    if per == 1:
        H = int(input("Hora: "))
        M = int(input("Minuto: "))
        S = int(input("Segundo: \n\n"))
        while H > -1 and H <= 23:
            print("{}:{}:{}" .format(H, M, S))
            S -= 1
            sleep(1)
            if S == -1:
                S = 59
                M -= 1
                if M == -1:
                    M = 59
                    H -= 1
            elif H == 0 and M == H and S == M:
                print("{}:{}:{}" .format(H, M, S))
                sleep(1)
                print("\nTempo alcançado...\n")
                sleep(2)
                pergunta = int(input("Deseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
                if pergunta == 1:
                    H = int(input("Hora: "))
                    M = int(input("Minuto: "))
                    S = int(input("Segundo: \n\n"))
                elif pergunta < 1 and pergunta > 1:
                    break
elif M < -1 or M > 59:
    print("O padrão do 'minuto' é de 0 a 59")
    sleep(1)
    per = int(input("\nQuer tentar novamente?\n [1] - Sim\n [2] - Não\n\n"))
    if per == 1:
        H = int(input("Hora: "))
        M = int(input("Minuto: "))
        S = int(input("Segundo: \n\n"))
        while H > -1 and H <= 23:
            print("{}:{}:{}" .format(H, M, S))
            S -= 1
            sleep(1)
            if S == -1:
                S = 59
                M -= 1
                if M == -1:
                    M = 59
                    H -= 1
            elif H == 0 and M == H and S == M:
                print("{}:{}:{}" .format(H, M, S))
                sleep(1)
                print("\nTempo alcançado...")
                sleep(2)
                pergunta = int(input("\nDeseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
                if pergunta == 1:
                    H = int(input("Hora: "))
                    M = int(input("Minuto: "))
                    S = int(input("Segundo: \n\n"))
                elif pergunta < 1 and pergunta > 1:
                    break
elif S < -1 or S > 59:
    print("O padrão do 'segundo' é de 0 a 59")
    sleep(1)
    per = int(input("\nQuer tentar novamente?\n [1] - Sim\n [2] - Não\n\n"))
    if per == 1:
        H = int(input("Hora: "))
        M = int(input("Minuto: "))
        S = int(input("Segundo: "))
        S = int(input("Segundo: \n\n"))
        while H > -1 and H <= 23:
            print("{}:{}:{}" .format(H, M, S))
            S -= 1
            sleep(1)
            if S == -1:
                S = 59
                M -= 1
                if M == -1:
                    M = 59
                    H -= 1
            elif H == 0 and M == H and S == M:
                print("{}:{}:{}" .format(H, M, S))
                sleep(1)
                print("\nTempo alcançado...")
                sleep(2)
                pergunta = int(input("\nDeseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
                if pergunta == 1:
                    H = int(input("Hora: "))
                    M = int(input("Minuto: "))
                    S = int(input("Segundo: \n\n"))
                elif pergunta < 1 and pergunta > 1:
                    break
while H > -1 and H <= 23:
    if H < -1 or H > 23:
        print("O padrão da 'hora' é de 0 a 23")
        sleep(1)
        per = int(input("\nQuer tentar novamente?\n [1] - Sim\n [2] - Não\n\n"))
        if per == 1:
            H = int(input("Hora: "))
            M = int(input("Minuto: "))
            S = int(input("Segundo: \n\n"))
            while H > -1 and H <= 23:
                print("{}:{}:{}" .format(H, M, S))
                S -= 1
                sleep(1)
                if S == -1:
                    S = 59
                    M -= 1
                    if M == -1:
                        M = 59
                        H -= 1
                elif H == 0 and M == H and S == M:
                    print("{}:{}:{}" .format(H, M, S))
                    sleep(1)
                    print("\nTempo alcançado...")
                    sleep(2)
                    pergunta = int(input("\nDeseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
                    if pergunta == 1:
                        H = int(input("Hora: "))
                        M = int(input("Minuto: "))
                        S = int(input("Segundo: \n\n"))
                    elif pergunta < 1 and pergunta > 1:
                        break
    elif M < -1 or M > 59:
        print("O padrão do 'minuto' é de 0 a 59")
        sleep(1)
        per = int(input("\nQuer tentar novamente?\n [1] - Sim\n [2] - Não\n\n"))
        if per == 1:
            H = int(input("Hora: "))
            M = int(input("Minuto: "))
            S = int(input("Segundo: \n\n"))
            while H > -1 and H <= 23:
                print("{}:{}:{}" .format(H, M, S))
                S -= 1
                sleep(1)
                if S == -1:
                    S = 59
                    M -= 1
                    if M == -1:
                        M = 59
                        H -= 1
                elif H == 0 and M == H and S == M:
                    print("{}:{}:{}" .format(H, M, S))
                    sleep(1)
                    print("\nTempo alcançado...")
                    sleep(2)
                    pergunta = int(input("\nDeseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
                    if pergunta == 1:
                        H = int(input("Hora: "))
                        M = int(input("Minuto: "))
                        S = int(input("Segundo: \n\n"))
                    elif pergunta < 1 and pergunta > 1:
                        break
    elif S < -1 or S > 59:
        print("O padrão do 'segundo' é de 0 a 59")
        sleep(1)
        per = int(input("\nQuer tentar novamente?\n [1] - Sim\n [2] - Não\n\n"))
        if per == 1:
            H = int(input("Hora: "))
            M = int(input("Minuto: "))
            S = int(input("Segundo: \n\n"))
            while H > -1 and H <= 23:
                print("{}:{}:{}" .format(H, M, S))
                S -= 1
                sleep(1)
                if S == -1:
                    S = 59
                    M -= 1
                    if M == -1:
                        M = 59
                        H -= 1
                elif H == 0 and M == H and S == M:
                    print("{}:{}:{}" .format(H, M, S))
                    sleep(1)
                    print("\nTempo alcançado...")
                    sleep(2)
                    pergunta = int(input("\nDeseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
                    if pergunta == 1:
                        H = int(input("Hora: "))
                        M = int(input("Minuto: "))
                        S = int(input("Segundo: \n\n"))
                    elif pergunta < 1 and pergunta > 1:
                        break
    print("{}:{}:{}" .format(H, M, S))
    S -= 1
    sleep(1)
    if S == -1:
        S = 59
        M -= 1
        if M == -1:
            M = 59
            H -= 1
    elif H == 0 and M == H and S == M:
        print("{}:{}:{}" .format(H, M, S))
        sleep(1)
        print("\nTempo alcançado...")
        sleep(2)
        pergunta = int(input("\nDeseja continuar?\n[1] - Sim\n[2] - Não\n\n"))
        if pergunta == 1:
            H = int(input("Hora: "))
            M = int(input("Minuto: "))
            S = int(input("Segundo: \n\n"))
        elif pergunta < 1 and pergunta > 1:
           break
sleep(1)
print("\nSaindo do programa...")
sleep(5)

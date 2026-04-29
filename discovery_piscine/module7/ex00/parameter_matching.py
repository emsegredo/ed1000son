import sys
from time import sleep

num_of_param = len(sys.argv) - 1

if num_of_param == 1:
    text = input("What was the parameter? : ")
    print("Scaning text and parameter...")
    sleep(2.5)
   
    if text == sys.argv[1]:
        print("Goog job!")
    
    else:
        print("Nope, sorry...")

else:
    print("none")
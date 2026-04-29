numb1 = int(input("Enter the first number : "))
numb2 = int(input("Enter the second number: "))

result = numb1 * numb2

if result > 0:
    print(f'\n{numb1} x {numb2} = {result}\nThe result is positive.')

elif result < 0:
    print(f'\n{numb1} x {numb2} = {result}\nThe result is negative.')

else:
    print(f'\n{numb1} x {numb2} = {result}\nThe result is positive and negative.')

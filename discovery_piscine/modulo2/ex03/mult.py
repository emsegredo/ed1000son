numb_1 = int(input("Enter the first number : "))
numb_2 = int(input("Enter the second number : "))

result = numb_1 * numb_2

if result > 0:
    print(f'{numb_1} x {numb_2} = {result}\nThe result is positive.')

elif result < 0:
    print(f'{numb_1} x {numb_2} = {result}\nThe result is negative.')

else:
    print(f'{numb_1} x {numb_2} = {result}\nThe result is positive and negative.')
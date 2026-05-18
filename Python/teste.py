def function(x):
    for i in range(1, 5):
        fat = 1
        fat *= x
        x -= 1 
        return fat

print(function(4))
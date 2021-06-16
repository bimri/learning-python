y = 101                                         # change this to get different results of the below code
x = y // 2
while x > 1:
    if y % x == 0:                              # Remainder
        print(y, 'has factor', x)
        break                                   # skip else
    x -= 1
else:                                           # if you don’t hit the break, the number is prime
    print(y, 'is prime')


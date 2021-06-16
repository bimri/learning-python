# statement causes an immediate jump to the top of a loop continue

x = 10
while x:
    x -= 1
    if x % 2 !=0: continue                          # Odd?--skip print
    print(x, end=' ')

print()

x = 10
while x:
    x -= 1
    if x % 2 ==0:                                   # Even?--print
        print(x, end=' ')

print()

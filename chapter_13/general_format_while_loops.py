'''
while test:                                     # Loop test
    statements                                  # Loop body
else:                                           # Optional else
    statements                                  # Run if didn't exit loop break
'''

# infinite loop
# while True:
#     print('Type Ctrl-C to stop me!')


# slicing
x = 'spam'
while x:                                            # While x is not empty
    print(x, end=' ')                               # end=' ' keyword argument used here to place all outputs on the same line
    x = x[1:]                                       # Strip first character off x

print()                                             # New for console output to skip to new line

# One way to code counter loops
a=0; b=10
while a < b:
    print(a, end=' ')
    a += 1

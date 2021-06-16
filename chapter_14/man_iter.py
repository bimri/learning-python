# Manual iteration - apply the iteration protocol

L = [1, 3, 4]

for X in L:                             # Automatic iteration
    print(X ** 2, end=' ')              # Obtains iter, calls __next__, catches exceptions

print('\n')

# Manual iteration: what for loops usually do
i  = iter(L)
while True:
    try:                                # try statement catches exceptions
        X = next(i)                     # Or call I.__next__ in 3.X
    except StopIteration:
        break
    print( X ** 2, end=' ')
    
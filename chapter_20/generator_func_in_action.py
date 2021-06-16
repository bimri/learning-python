def gensquares(N):
    for i in range(N):
        yield i ** 2            # Resume here later

for i in gensquares(5):         # Resume the function
    print(i, end=' : ')         # Print last yielded value


'''
To end the generation of values, functions either use a return statement with no value
or simply allow control to fall off the end of the function body.
'''

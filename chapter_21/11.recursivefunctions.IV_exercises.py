def countdown(N):
    if N == 0:
        print('stop')
    else:
        print(N, end=' ')
        countdown(N-1)

countdown(10)
countdown(90)


# generator-based solution
def countdown2(N):                                                          # Generator function, recursive
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N-1): yield x                                   # 3.3+: yield from countdown2(N-1)

print(list(countdown2(5)))


# Nonrecursive options:
def countdown3():                                                           # Generator function, simpler
    yield from range(5, 0, -1)                                              # Pre 3.3: for x in range(): yield x

print(list(countdown3()))
print(list(x for x in range(5, 0, -1)))                                     # Equivalent generator expression   
print(list(range(5, 0, -1)))                                                # Equivalent nongenerator form

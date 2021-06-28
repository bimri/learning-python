from squares_yield import Squares                       # Using the __iter__/yield Squares

S = Squares(1, 5)
I = iter(S)
print(next(I), next(I))

J = iter(S)                                             # With yield, multiple iterators automatic
print(next(J))
print(next(I))                                          # I is independent of J: own local state


"""
Although generator functions are single-scan iterables, the implicit calls to __iter__ in
iteration contexts make new generators supporting new independent scans:
"""
S = Squares(1, 3)

for i in S:                                             # Each for calls __iter__
    for j in S:
        print('%s:%s' % (i, j), end=' ')
        
# range allows multiple iterators
R = range(3)
# next(R)                                           # TypeError: range object is not an iterator

I1 = iter(R)
print(next(I1))
print(next(I1))

I2 = iter(R) # Two iterators on one range
print(next(I2))
print(next(I2))                                     # I1 is at a different spot than I2


'''
zip, map, and filter do not support multiple active iterators on the same result
'''
Z = zip((1, 2, 3), (10, 11, 12))

I1 = iter(Z)
I2 = iter(Z)                                        # Two iterators on one zip

print(next(I1))
print(next(I1))

print(next(I2))


M = map(abs, (-1, 0, 1)) # Ditto for map (and filter)
I1 = iter(M); I2 = iter(M)

print(next(I1), next(I1), next(I1))                         # (3.X) Single scan is exhausted!
# print(next(I2))


R = range(3) # But range allows many iterators
I1, I2 = iter(R), iter(R)

print(
    [next(I1), next(I1), next(I1)]
)
print(
    next(I2)                                                # Multiple active scans, like 2.X lists
)
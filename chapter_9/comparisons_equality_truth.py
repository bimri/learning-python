L1 = [1, ('a', 3)]                      # Same value, unique objects
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)                      # Equivalent? Same object?

# is operator tests object identity
# i.e., live at the same address in memory

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S2 is S1)                               # Python internally caches


S1 = 'a longer string forever and ever'
S2 = 'a longer string forever and ever'
print(S1 == S2, S1 is S2)                                # AGAIN cached by Python


# Relative magnitude comparisons
L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)                       # Less, equal, greater: tuples of results


# mixed-type comparisons and sorts
print(11 == '11')                                       # 3.X: equality works but magnitude does not
# 11 >= '11'                                            # Error

print(['11', '22'].sort())                              # Ditto for sorts
# [11, '11'].sort()                                     # Error

print(11 > 9.123)                                       # Mixed numbers convert to highest type
print(str(11) >= '11', 11 >= int('11'))                 # Manual conversions force the issue


# dictionary comparisons
D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}

print(D1 == D2)
# D1 < D2                                                 # unordered types: TypeError


# compare the sorted key/value lists manually
print(list(D1.items()))
print(sorted(D1.items()))

print(sorted(D1.items()) < sorted(D2.items()))              # Magnitude test in 3.X
print(sorted(D1.items()) > sorted(D2.items()))

D = {}
D[1] = 'a'
D[2] = 'b'

print(D)


'''Any immutable object can be used as a dictionary key, including
integers, tuples, strings, and so on'''

D[(1,2,3)] = 'c'
print(D)

'''
When you use lists, it is illegal to assign to an 
offset that is off the end of the list
'''

# L = []
# print(L[99] = 'spam')                 # generates IndexError: list assignment index out of range


# Usage of repetition to preallocate as big a list
L = [0]*100
print(L)

# Preallocate a dictionary as above
D = {}
D[99] = 'spam'
print(D[99])


# keys are intergers
table = {
    1975: 'Holy Grail',
    1979: 'Life of Brian',
    1983: 'The Meaning of Life'
}

print(table[1975])

print(list(table.items()))

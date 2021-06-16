'''every time you index a string, you get back a string that can
be indexed again'''
S = 'spam'

# S[0][0][0][0][0] just keeps 
# indexing the first character over and over
print(S[0][0][0][0][0])


'''This generally doesn’t work for lists (lists can hold arbitrary objects) unless
the list contains strings'''
S = ['s', 'p', 'a', 'm']
print(S[0][0][0][0][0])

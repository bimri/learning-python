S = 'spam'

result = S.find('pa')
print(result)


M = 'spammy'
M = M.replace('mm', 'xx')
print(M)


# Search for position
V = 'xxxxSPAMxxxxSPAMxxxx'
where = V.find('SPAM')              # Occurs at offset 4
print(where)

V = V[:where] + 'EGGS' + V[(where+4):]
print(V)


L = list(M)
print(L)

L[3] = 'm'
L[4] = 'm'
print(L)

R = ''.join(L)          # convert from list back to string
print(R)


# JOIN method
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

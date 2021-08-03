"Unicode literals in 3.3"
# normal strings are unicode in 3.X

U = u'coding'                           # 2.X Unicode literal accepted in 3.3+
print(type(U))                          # It is just str, but is backward compatible
print(U)
print(U[0])
print(list(U))
print()


"Python 2.X String Literals"
B = b'bimri'                            # 3.X bytes literal is just str in 2.6/2.7
S = 'Literals'                          # str is a bytes/character sequence

print(type(B)); print(type(S))
print(B); print(S)
print(B[0]); print(S[0])
print(list(B)); print(list(S))
print()

'In 2.X the special Unicode literal and type accommodates richer forms of text:'
U = u'codes'                            # 2.X Unicode literal maks a distinct type
print(type(U))                          # Works in 3.3 too, but is just a str here

# for compatibility this form works in 3.3 and later too, but it simply makes a normal str there (the u is ignored).
print(U)
print(U[2])
print(list(U))

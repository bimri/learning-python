A = 'spam'
B = A
B = 'Shrubbery'                 # B is reset to point to new string

print(A, B)

B = B + 'Shrubbery'
print(B)


X = ['spam']
Y = X
Y[0] = 'shrubbery'              # Changed object that both reference by overwriting it in place

print(X, Y)


T = ['time']
W = T[:]                        # Copy list T
W[0] = 'sands'                  # Only changes it copy of list T; original T remains unaltered

print(T, W)

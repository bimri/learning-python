# range and len
S = 'spam'
for i in range(len(S)):                 # repeat counts 0..3
    S = S[1:] + S[:1]                   # move front item to end
    print(S, end=' ')
print()

print(S)

for i in range(len(S)):                 # for positions 0..3
    X = S[i:] + S[:i]                   # rear part + front part
    print(X, end=' ')
print()

# Works on any sequence type
L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]
    print(X, end=' ')
print()

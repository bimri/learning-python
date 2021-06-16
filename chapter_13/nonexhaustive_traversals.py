# use this technique to skip items as we go:
S = 'abcdefghijk'
print(
    list(range(0, len(S), 2))
)

for i in range(0, len(S), 2): print(S[i], end=' ')
print()

# slice with a stride of 2
for c in S[::2]: print(c, end=' ')

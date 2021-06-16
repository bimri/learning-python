S = "spam"

# assignment that changes the string to "slam", 
# using only slicing and concatenation
S = S[0] + 'l' + S[2:]
print(S)


# using just indexing and concatenation
S = S[0] + 'l' + S[2] + S[3]
print(S)

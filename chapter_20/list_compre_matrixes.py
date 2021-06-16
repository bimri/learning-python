"multidimensional arrays == matrixes"
M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

N = [[2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]]

# we can always index rows, and columns within rows, 
# using normal index operations
print(M[1])                         # Row 2
print(M[1][2])                      # Row 2, item 3


# automatically scan rows and columns
col2 = [row[1] for row in M]
print(col2)

offsets = [M[row][1] for row in (0, 1, 2)]
print(offsets)

diagonals = [M[i][i] for i in range(len(M))]
print(diagonals)

diagonals = [M[i][len(M)-1-i] for i in range(len(M))]
print(diagonals)


# Changing such a matrix in place requires assignment to offsets
L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j] += 10

print(L)


# Assign to M to retain new value
nv = [col + 10 for row in M for col in row]
print(nv)

nvw = [[col + 10 for col in row] for row in M]
print(nvw)

'# Statement equivalents'
res = []

for row in M:
    for col in row:                     # Indent parts further right
        res.append(col + 10)

print(res)


res = []
for  row in M:
    tmp = []                            # Left-nesting starts new list
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)

print(res)


[M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]

# equivalent to
res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)

'zip to pair items to be multiplied'
[[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]

res = []
for (row1, row2) in zip(M, N):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)


"code conciseness is a much less important goal than code readability"
# Keep it simple sir(KISS)


'''
map calls can be twice as fast
as equivalent for loops, and list comprehensions are often faster than map calls

map and list comprehensions run at C language speed inside the interpreter which
is often much faster than stepping through Python for loop bytecode within the PVM
'''
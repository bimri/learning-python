'''
Errors for nonexistent key fetches are common in sparse matrixes:

    1. Test for key ahead of time in if statements
    2. Use try statement to catch & recover from the exception explicity
    3. Use the dictionary get method.

'''
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4

if (2, 3, 6) in Matrix:                             # Check for key before fetch
    print(Matrix[(2, 3, 6)])
else:
    print(0)


try:
    print(Matrix[(2, 3, 6)])                        # Try to index
except KeyError:                                    # Catch and recover
    print(0)


print(Matrix.get((2, 3, 4), 0))                     # Exists: fetch and return
print(Matrix.get((2, 3, 6), 0))                     # Doestn't exist: use default arg

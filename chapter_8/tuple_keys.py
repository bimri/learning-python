'''
dictionary keys are also commonly leveraged to implement 
sparse data structures
'''

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4                             # ';' separates statements
print(Matrix[(X, Y, Z)])

print(Matrix)

'''Normal and Chained'''

print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

X = 2
Y = 4
Z = 6

# Chained comparisons: range tests
print(X < Y < Z)
print(X < Y and Y < Z)

print(X < Y > Z)
print(X < Y and Y > Z)

print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)


# Numeric comparisons are based on magnitudes
print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))

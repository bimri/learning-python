T = (1, 2, 3, 4)
print(len(T))

print(T + (5,6))                # Concat
print(T[0])                     # Index


# Type-specific callable methods
print(T.index(4))               # tuple methods: 4 appears at offset 3
print(T.count(4))               # 4 appears once

# Make a new tuple for a new value
T = (2,) + T[1:]
print(T)


# Tuples support mixed types and nesting
S = 'spam', 3.0, [11, 22, 33]
print(S[1])
print(S[2][1])

# generator expressions often are equivalent to 3.X calls map
" generator expressions may be simpler to code when the operation applied is not a function call "

# Map function on tuple
list(map(abs, (-1, -2, 3, 4)))

# Generator expression
list(abs(x) for x in (-1, -2, 3, 4))

# Nonfunction case
list(map(lambda x: x * 2, (1, 2, 3, 4)))

# Simpler as generator?
list(x * 2 for x in (1, 2, 3, 4))


'''
The same holds true for text-processing use cases like the join call we saw earlier—a
list comprehension makes an extra temporary list of results, which is completely pointless
in this context because the list is not retained, and map loses simplicity points compared
to generator expression syntax when the operation being applied is not a call:
'''
line = 'aaa;bbb;ccc'

# Makes a pointless list
print(
    ''.join([x.upper() for x in line.split(';')])       # Makes a pointless list
)

# Generates results
print(
    ''.join(x.upper() for x in line.split(';'))
)

# Generates results
print(
    ''.join(map(str.upper, line.split(';')))
)

# Simpler as generator?
print(
    ''.join(x * 2 for x in line.split(';'))
)

print(
    ''.join(map(lambda x: x * 2, line.split(';')))
)


'''
Both map and generator expressions can also be arbitrarily nested, which supports general
use in programs, and requires a list call or other iteration context to start the
process of producing results.
'''
# Nested comprehensions
print(
    [x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]
)

# Nested maps
print(
    list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4))))
)

# Nested generators
print(
    list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4)))
)
"Although the effect of all three of these is to combine operations, the generators do so without making multiple temporary lists."


# Nested combinations
import math

print(
    list(map(math.sqrt, (x ** 2 for x in range(4))))
)

"nonnested approaches provide simpler solutions but still leverage generators’ strengths —per a Python motto"
# Unnested equivalents
list(abs(x) * 2 for x in (-1, -2, 3, 4))

# Flat is often better
list(math.sqrt(x ** 2) for x in range(4))
list(abs(x) for x in (-1, 0, 1))

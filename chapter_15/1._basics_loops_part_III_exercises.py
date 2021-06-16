# 1.A For loop that prints ASCII code of each character in 
# a string named S. Using built-in function "ord(charater)"

S = 'bimri'

for x in S:
    print(ord(x))


# Compute the sum of all ASCII codes in the S string
x = 0

for c in S: 
    x +=  ord(c)
print(x)


# return a new list that contains the ASCII codes of each character
x = []

for c in S:
    x.append(ord(c))
print(x)


print(
    list(map(ord, S))                                       # functional way to achieve similar results
)


print(
    [ord(c) for c in S]                                     # List comprehension to achieve same result
)

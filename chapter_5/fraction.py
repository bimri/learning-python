from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)


# Fraction objects can also be created from 
# floating-point number strings, much like decimals
print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))

import math 

print(math.floor(2.5))                  # Closest number below value
print(math.floor(-2.5))                 
print(math.trunc(2.5))                  # Truncate fractional part(towards zero)
print(math.trunc(-2.5))


print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)
print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)


# Truncation toward zero regardless of sign
print(math.trunc(5 / -2))


"Classic, Floor, and True"

# X / Y  --> Classic and True division
# Always keeping remainders in floating-point results, regardless of types.

# X // Y --> Floor division
# Always truncates frational remainders down to their floor, regardless of types.

print(10 / 4)                       # keeps remainder
print(10 / 4.0)                     # keeps remainder
print(10 // 4)                      # truncates remainder
print(10 // 4.0)                    # truncates to floor

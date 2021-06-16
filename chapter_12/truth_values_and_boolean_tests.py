'''
In Python:
    - All objects have an inherent Boolean true or false value
    - Any nonzero number or nonempty object is true
    - Zero numbers, empty objects, and the special object None 
      are considered false
    - Comparisons and equality tests are applied recursively to 
      data structures
    - Comparisons and equality tests return True or False 
      (custom versions of 1 and 0)
    - Boolean and and or operators return a true or false 
      operand object
    - Boolean operators stop evaluating (“short circuit”) as 
      soon as a result is known
'''

# Boolean expression operators in Python
X = Y = 0

X and Y                 # Is true if both X and Y are true
X or Y                  # Is true if either X or Y is true
not X                   # Is true if X is false (the expression returns True or False)

print(2 < 3, 3< 2)


# OR test --> evaluated from L to R; returns first one that is true
print(2 or 3, 3 or 2)                                   # return left operand if true
                                                        # Else, return right operand (true or false)
print([] or 3)
print([] or {})
print({} or [])

# print("x" + 1)                                                                            # TypeError: can only concatenate str (not "int") to str
# print({} + {})                                                                            # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# append method works only for lists, not strings
'''append assumes its target is mutable, since it’s an in-place extension;
strings are immutable.'''
[].append(9)
# ''.append('s')                                                                            # AttributeError: 'str' object has no attribute 'append'

# keys works only on dictionaries
print(list({}.keys()))                                                                      # list() needed in 3.X
# [].keys()                                                                                 # AttributeError: 'list' object has no attribute 'keys'


'''Slicing and concatenation always return a new object of the same type as the
objects processed'''
[][:]
""[:]

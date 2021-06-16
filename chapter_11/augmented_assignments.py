'''Borrowed from C, these formats are mostly just shorthand'''
# They imply the combination of a binary expression and an assignment
# X = X + 1                                               # Traditional form
# X += 1                                                  # Newer augmented form


'''
Augmented assignment statements: - 
X += Y      X &= Y      X −= Y      X |= Y
X *= Y      X ^= Y      X /= Y      X >>= Y
X %= Y      X <<= Y     X **= Y     X //= Y
'''

'''Augmented assignment works on any type 
that supports the implied binary expression'''
x = 1                                                       # traditional
x = x + 1
print(x)

x += 1                                                      # Augmented
print(x)


# Implied concatenation: STRINGS
S = "spam"
S += " SPAM"
print(S)


# Concatenate: slower
L = [1, 2]
L = L + [3]
print(L)

# Faster, but in place
L.append(4)
print(L)


# add a set of items to the end
L = L + [5, 6]                                          # Concatenate: slower
print(L)

L.extend([7, 8])                                        # Faster, but in place
print(L)


# use augmented assignment to extend a list
L += [9, 10]                                            # Mapped to L.extend([9, 10])
print(L)


'''equivalence += for a list is not exactly the same as a
+ and = in all cases—for lists += allows arbitrary sequences (just like extend), but concatenation
normally does not'''
L = []
L += 'spam'                                             # += and extend allow any sequence, but + does not!

print(L)

# L = L + 'spam'                                        # TypeError: can only concatenate list (not "str") to list


'''Augmented assignment and shared references'''
L = [1, 2]
M = L                                                   # L and M reference the same object
L = L + [3, 4]                                          # Concatenation makes a new object
print(L, M)                                             # Changes L but not M

L = [1, 2]
M = L 
L += [3, 4]                                             # But += really means extend
print(L, M)                                             # M sees the in-place change too!

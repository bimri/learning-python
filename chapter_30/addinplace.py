"In-Place Addition"
'''
To also implement += in-place augmented addition, code either an __iadd__ or an
__add__.
'''
class Number:
    def __init__(self, val):
        self.val = val 
    def __iadd__(self, other):                              # __iadd__ explicit: x += y
        self.val += other                                   # Usually returns self 
        return self 


if __name__ == "__main__":
    x = Number(5)
    x += 1
    x += 1

    print(x.val)

    # For mutable objects, this method can often specialize for quicker in-place changes:
    y = Number([1])                     # In-place change faster than + 
    y += [2]
    y += [3]

    print(y.val)


'''
The normal __add__ method is run as a fallback, but may not be able optimize in-place
cases:
'''
class Number:
    def __init__(self, val):
        self.val = val 
    def __add__(self, other):                             # __add__ fallback: x = (x + y)
        return Number(self.val + other)                   # Propagates class type 
        

if __name__ == "__main__":
    x = Number(5)
    x += 1
    x += 1                                  # And += does concatenation here

    print(x.val)



"""
Though we’ve focused on + here, keep in mind that every binary operator has similar
right-side and in-place overloading methods that work the same (e.g., __mul__,
__rmul__, and __imul__). Still, right-side methods are an advanced topic and tend to be
fairly uncommon in practice; you only code them when you need operators to be commutative,
and then only if you need to support such operators at all. For instance, a
Vector class may use these tools, but an Employee or Button class probably would not.
"""

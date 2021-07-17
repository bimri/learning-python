"Extending types by Subclassing "
'''
The following class, coded in the file setsubclass.py, customizes lists to add just methods
and operators related to set processing. Because all other behavior is inherited from the
built-in list superclass, this makes for a shorter and simpler alternative—everything
not defined here is routed to list directly:
'''

class Set(list):
    def __init__(self, value = []):                             # Constructor
        list.__init__([])                                       # Customizes list
        self.concat(value)                                      # Copies mutable object

    def intersect(self, other):                                 # other is any sequence
        res = []                                                # self is the subject
        for x in self:
            if x in other:                                      # Look for each item in other
                res.append(x)                                   # Add to result if found
        return Set(res)                                         # Return result(a new Set)
    
    def union(self, other):                                     # other is any sequence
        res = Set(self)                                         # Copy me and my list   
        res.concat(other)                                       # Add the other items not already in me
        return res                                              # Return the new Set
    
    def concat(self, value):                                    # value: list, Set, etc.
        for x in value:                                         # Removes duplicates
            if not x in self:
                self.append(x)                                 # Add new items
            
    def __and__(self, other): return self.intersect(other)       # self & other
    def __or__(self, other): return self.union(other)            # self | other
    def __repr__(self): return 'Set:' + list.__repr__(self)     # For the interactive prompt


if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)

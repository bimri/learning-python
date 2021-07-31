"Why Exception Hierarchies?"
# Catch any of these
try: 
    func() 
except (General, Specific1, Specific1):
    ...


'''
This approach worked for the defunct string exception model too. For large or high
exception hierarchies, however, it may be easier to catch categories using class-based
categories than to list every member of a category in a single except clause. Perhaps
more importantly, you can extend exception hierarchies as software needs evolve by
adding new subclasses without breaking existing code.
'''

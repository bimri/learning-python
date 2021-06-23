__all__ = ['a', '_c']                                       # __all__ has precedence over _X
a, b, _c, _d = 1, 2, 3, 4


'''
>>> from alls import *                                      # Load __all__ names only
>>> a, _c
(1, 3)
>>> b
NameError: name 'b' is not defined

>>> from alls import a, b, _c, _d                           # But other importers get every name
>>> a, b, _c, _d
(1, 2, 3, 4)

>>> import alls
>>> alls.a, alls.b, alls._c, alls._d
(1, 2, 3, 4)
'''


"""
Like the _X convention, the __all__ list has meaning only to the from * statement form
and does not amount to a privacy declaration: other import statements can still access
all names, as the last two tests show.
"""
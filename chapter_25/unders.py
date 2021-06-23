a, _b, c, _d = 1, 2, 3, 4

'''
>>> from unders import *                                    # Load non _X names only
>>> a, c
(1, 3)
>>> _b
NameError: name '_b' is not defined

>>> import unders                                           # But other importers get every name
>>> unders._b
2
'''

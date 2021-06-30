"Boolean Tests: __bool__ and __len__"
'''
every object is inherently true or false in Python. When you code classes, you can define what
this means for your objects by coding methods that give the True or False values of
instances on request.

in Boolean contexts, Python first tries __bool__ to obtain
a direct Boolean value; if that method is missing, Python tries __len__ to infer a truth
value from the object’s length.
'''
class Truth:
    def __bool__(self): return True


if __name__ == "__main__":
    X = Truth()
    if X: print('yes!')


class Truth:
    def __bool__(self): return False


if __name__ == "__main__":
    X = Truth()
    print(bool(X))



"""
If this method is missing, Python falls back on length because a nonempty object is
considered true (i.e., a nonzero length is taken to mean the object is true, and a zero
length means it is false):
"""
class Truth:
    def __len__(self): return 0


if __name__ == "__main__":
    X = Truth()
    if not X: print('no!')



"""
If both methods are present Python prefers __bool__ over __len__, because it is more
specific:
"""
class Truth:
    def __bool__(self): return True
    def __len__(self): return 0


if __name__ == "__main__":
    X = Truth()
    if X: print('yes!')



"""
If neither truth method is defined, the object is vacuously considered true
    >>> class Truth:
            pass
    >>> X = Truth()
    >>> bool(X)
    True
"""

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):                   # By name, not built-in
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)


class SubMeta(SuperMeta):                                               # Created by type default
        def __init__(Class, classname, supers, classdict):              # Overrides type.__init__
            print('In SubMeta init:', classname)


print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)                                                 # Not a data descriptor if found by name
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})                                # Explicit calls work: class inheritance
print()
SubMeta('yyy', (), {})                                                  # But implicit built-in calls do not: type


"""
Of course, this specific example is a special case: catching a built-in run on a metaclass,
a likely rare usage related to __call__ here. But it underscores a core asymmetry and
apparent inconsistency: normal attribute inheritance is not fully used for built-in dispatch
—for both instances and classes.
"""

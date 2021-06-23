"Example: Modules Are Objects"
'''
Because modules expose most of their interesting properties as built-in attributes, it’s
easy to write programs that manage other programs. We usually call such manager
programs metaprograms because they work on top of other systems. This is also referred
to as introspection, because programs can see and process object internals.

Python also exports the list of all loaded
modules as the sys.modules dictionary and provides a built-in called getattr that lets
us fetch attributes from their string names—it’s like saying object.attr, but attr is an
expression that yields a string at runtime.

By exposing module internals like this, Python helps you build programs about programs.
'''



#!python
"""
mydir.py: a module that lists the namespaces of other modules
"""
seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)
    
    count = 0
    for attr in sorted(module.__dict__):                                    # Scan namespace keys (or enumerate)
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<built-in name>')                                        # Skip __file__, etc.
        else:
            print(getattr(module, attr))                                    # Same as .__dict__[attr]
        count += 1
    
    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)


if __name__ == '__main__':
    import mydir 
    listing(mydir)                                                          # self-test code: list itself


'''
To use this as a tool for listing other modules, simply pass the modules in as objects to
this file’s function.
'''

"""
>>> import mydir
>>> import tkinter
>>> mydir.listing(tkinter)
------------------------------------------------------------
name: tkinter file: C:\Python33\lib\tkinter\__init__.py
------------------------------------------------------------
00) ACTIVE active
01) ALL all
02) ANCHOR anchor
03) ARC arc
04) At <function At at 0x0000000002BD41E0>
...many more names omitted...
156) image_types <function image_types at 0x0000000002BE2378>
157) mainloop <function mainloop at 0x0000000002BCBBF8>
158) sys <module 'sys' (built-in)>
159) wantobjects 1
160) warnings <module 'warnings' from 'C:\\Python33\\lib\\warnings.py'>
------------------------------------------------------------
tkinter has 161 names
------------------------------------------------------------


The point to notice here is that mydir
is a program that lets you browse other programs. Because Python exposes its internals,
you can process objects generically.
"""

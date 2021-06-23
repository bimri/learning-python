"""
Both the import and from statements were eventually extended to allow an imported
name to be given a different name in your script.
    import modulename as name                                   # And use name, not modulename

is equivalent to the following, which renames the module in the importer’s scope only
(it’s still known by its original name to other files):
        import modulename
        name = modulename
        del modulename                                          # Don't keep original name

After such an import, you can—and in fact must—use the name listed after the as to
refer to the module. This works in a from statement, too, to assign a name imported
from a file to a different name in the importer’s scope; as before you get only the new
name you provide, not its original:
    from modulename import attrname as name                     # And use name, not attrname

this extension is commonly used to provide short synonyms
for longer names, and to avoid name clashes when you are already using a name
in your script that would otherwise be overwritten by a normal import statement:
    import reallylongmodulename as name                         # Use shorter nickname
    name.func()

    from module1 import utility as util1                        # Can have only 1 "utility"
    from module2 import utility as util2
    util1(); util2()

It also comes in handy for providing a short, simple name for an entire directory path
and avoiding name collisions when using the package import
    import dir1.dir2.mod as mod # Only list full path once
    mod.func()

    from dir1.dir2.mod import func as modfunc                   # Rename to make unique if needed
    modfunc()    

This is also something of a hedge against name changes: if a new release of a library
renames a module or tool your code uses extensively, or provides a new alternative
you’d rather use instead, you can simply rename it to its prior name on import to avoid
breaking your code:
    import newname as oldname
    from library import newname as oldname
    ...and keep happily using oldname until you have time to update all your code...
"""

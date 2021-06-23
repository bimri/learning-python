'''
from mymod import countLines, countChars
print(countLines('mymod.py), countChars('mymod.py))

% python myclient.py
13 346
'''

"""
As for the rest of this one, mymod’s functions are accessible (that is, importable) from
the top level of myclient, since from simply assigns to names in the importer (it
works as if mymod’s defs appeared in myclient). For example, another file can say:
    import myclient
    myclient.countLines(...)

    from myclient import countChars
    countChars(...)

If myclient used import instead of from, you’d need to use a path to get to the
functions in mymod through myclient:
    import myclient
    myclient.mymod.countLines(...)

    from myclient import mymod
    mymod.countChars(...)

In general, you can define collector modules that import all the names from other
modules so they’re available in a single convenience module. The following partial
code, for example, creates three different copies of the name somename—mod1.some
name, collector.somename, and __main__.somename; all three share the same integer
object initially, and only the name somename exists at the interactive prompt as is:
    # File mod1.py
    somename = 42

    # File collector.py
    from mod1 import * # Collect lots of names here
    from mod2 import * # from assigns to my names
    from mod3 import *
    
    >>> from collector import somename
"""
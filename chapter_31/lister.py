"Collector module"
'''
we can provide a collector module
that combines them in a single namespace—importing just the following gives access
to all three lister mix-ins at once
'''
from listinstance   import ListIntance 
from listinherited import ListInherited
from listtree      import ListTree

Lister = ListTree                           # Choose a default lister 



"""
Importers can use the individual class names as is, or alias them to a common name
used in subclasses that can be modified in the import statement:
    >>> import lister
    >>> lister.ListInstance # Use a specific lister
    <class 'listinstance.ListInstance'>
    >>> lister.Lister # Use Lister default
    <class 'listtree.ListTree'>
    
    >>> from lister import Lister # Use Lister default
    >>> Lister
    <class 'listtree.ListTree'>
    
    >>> from lister import ListInstance as Lister # Use Lister alias
    >>> Lister
    <class 'listinstance.ListInstance'>
"""

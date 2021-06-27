"there are two ways to load a class from a file"
'''
import person                                               # Load class with import
bob = person.Person(...)                                    # Go through module name

from person import Person, Manager                          # Load class with from
sue = Person(...)                                           # Use name directly
'''

# store Person objects on a shelve database
from person import Person, Manager                          # Load our classes
bimri = Person('Bimri Codes')                               # Re-recreate objects to be stored
bati  = Person('Bati Reads', job='reader', pay=90000)
jenny = Manager('Jenny Writes', 100000)

import shelve 
db = shelve.open('persondb')                                # Filename where objects are stored
for obj in (bimri, bati, jenny):                            # Use object's name attr as key
    db[obj.name] = obj                                      # Store object on shelve by key
db.close()                                                  # Close after making changes


'''
if this script has no output when run, it means it probably
worked; we’re not printing anything, just creating and storing objects in a file-based
database.
'''


"""
Python’s standard library glob module allows us to get directory listings
in Python code to verify the files here, and we can open the files in text or binary mode
to explore strings and bytes:

    >>> import glob
    >>> glob.glob('person*')
    ['person-composite.py', 'person-department.py', 'person.py', 'person.pyc',
    'persondb.bak', 'persondb.dat', 'persondb.dir']
    
    >>> print(open('persondb.dir').read())
    'Sue Jones', (512, 92)
    'Tom Jones', (1024, 91)
    'Bob Smith', (0, 80)
    
    >>> print(open('persondb.dat','rb').read())
    b'\x80\x03cperson\nPerson\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00jobq\x03NX\x03\x00
    ...more omitted...

"""


'''
Because shelves are Python objects containing Python objects, we can process them with
normal Python syntax and development modes.

    >>> import shelve
    >>> db = shelve.open('persondb')                                    # Reopen the shelve
    
    >>> len(db)                                                         # Three 'records' stored
    3
    >>> list(db.keys())                                                 # keys is the index
    ['Sue Jones', 'Tom Jones', 'Bob Smith']                             # list() to make a list in 3.X
    
    >>> bob = db['Bob Smith']                                           # Fetch bob by key
    >>> bob                                                             # Runs __repr__ from AttrDisplay
    [Person: job=None, name=Bob Smith, pay=0]
    
    >>> bob.lastName()                                                  # Runs lastName from Person
    'Smith'

    >>> for key in db:                                                  # Iterate, fetch, print
            print(key, '=>', db[key])
            
    Sue Jones => [Person: job=dev, name=Sue Jones, pay=100000]
    Tom Jones => [Manager: job=mgr, name=Tom Jones, pay=50000]
    Bob Smith => [Person: job=None, name=Bob Smith, pay=0]
    
    >>> for key in sorted(db):
            print(key, '=>', db[key])                                           # Iterate by sorted keys
    
    Bob Smith => [Person: job=None, name=Bob Smith, pay=0]
    Sue Jones => [Person: job=dev, name=Sue Jones, pay=100000]
    Tom Jones => [Manager: job=mgr, name=Tom Jones, pay=50000]
'''

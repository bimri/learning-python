"Why You Will Care: Classes and Persistence"
'''
# Python’s pickle and shelve object persistence
In fact, these tools are often compelling enough to motivate the use of classes in general—by pickling
or shelving a class instance, we get data storage that contains both data and logic combined.
'''
class SomeClass: ...
filename = ""

import pickle
obj = SomeClass()
file = open(filename, 'wb')             # Create external file 
pickle.dump(obj, file)                  # Save object in file 

import pickle 
file = open(filename, 'rb')
obj = pickle.load(file)                 # Fetch it back later


"""
Pickling converts in-memory objects to serialized byte streams (in Python, strings),
which may be stored in files, sent across a network, and so on; unpickling converts
back from byte streams to identical in-memory objects. Shelves are similar, but they
automatically pickle objects to an access-by-key database, which exports a dictionarylike
interface:
"""
import shelve 
obj = SomeClass()
dbase = shelve.open(filename)
dbase['key'] = obj                      # save under key

import shelve 
dbase = shelve.open(filename)
obj = dbase['key']                      # Fetch it back later


# Pizzashop example
from pizzashop import Pizzashop

shop = Pizzashop()
shop.server, shop.chef
# (<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>)

import pickle
pickle.dump(shop, open('shopfile.plk', 'wb'))

'''
This stores an entire composite shop object in a file all at once. To bring it back later in
another session or program, a single step suffices as well. In fact, objects restored this
way retain both state and behavior:
'''
import pickle 
obj = pickle.load(open('shopfile.pkl', 'rb'))
obj.server, obj.chef
# (<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>)

obj.order('LSP')
# LSP orders from <Employee: name=Pat, salary=40000>
# Bob makes pizza
# oven bakes
# LSP pays for item to <Employee: name=Pat, salary=40000>

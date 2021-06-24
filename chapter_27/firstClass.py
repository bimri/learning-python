class FirstClass:                           # Define a class object
    def setdata(self, value):               # Define class's methods
        self.data = value                   # self is the instance
    def display(self):
        print(self.data)                    # self.data: per instance
    
'''
# we have three objects: two instances and a class
>>> x = FirstClass()                            # Maket two instances
>>> y = FirstClass()                            # Each is a new namespace
'''

"""
The two instances start out empty but have links back to the class from which they
were generated. If we qualify an instance with the name of an attribute that lives in the
class object, Python fetches the name from the class by inheritance search (unless it
also lives in the instance):

>>> x.setdata("King Arthur")                    # Call methods: self is x
>>> y.setdata(3.14159)                          # Runs: FirstClass.setdata(y, 3.14159)


Neither x nor y has a setdata attribute of its own, so to find it, Python follows the link
from instance to class. And that’s about all there is to inheritance in Python: it happens
at attribute qualification time, and it just involves looking up names in linked objects
"""
  

'''
In the setdata function inside FirstClass, the value passed in is assigned to
self.data.

Within a method, self automatically refers to the instance being processed (x or y), so the assignments
store values in the instances’ namespaces, not the class’s 

Because classes can generate multiple instances, methods must go through the self
argument to get to the instance to be processed. 

>>> x.display()                                 # self.data differs in each instance
King Arthur
>>> y.display()                                 # Runs: FirstClass.display(y)
3.14159


As with everything else in Python, there are no
declarations for instance attributes (sometimes called members); they spring into existence
the first time they are assigned values, just like simple variables.
'''


"""
way to appreciate how dynamic this model is, consider that we can change
instance attributes in the class itself, by assigning to self in methods, or outside the
class, by assigning to an explicit instance object:

>>> x.data = "New value"                        # Can get/set attributes
>>> x.display()                                 # Outside the class too
New value    
"""


'''
Although less common, we could even generate an entirely new attribute in the instance’s
namespace by assigning to its name outside the class’s method functions:

>>> x.anothername = "spam"                      # Can set new attributes here too!
'''
 
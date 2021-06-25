# Add record field initialization
class Person: 
    def __init__(self, name, job, pay):                 # Construction takes three arguments
        self.name = name                                # Fill out fields when created
        self.job  = job                                 # self is the new instance object
        self.pay  = pay 


# Add defaults for constructor arguments
class Person:
    '''
    What this code means is that we’ll need to pass in a name when making Persons, but
    job and pay are now optional; they’ll default to None and 0 if omitted.
    '''
    def __init__(self, name, job=None, pay=0):          # Normal function args
        self.name = name 
        self.job  = job
        self.pay  = pay 
    

# Add incremental self-test code
# bob = Person('Bob Smith')                               # Test the class
# sue = Person('Sue Jones', job='dev', pay=100000)        # Runs __init__ automatically
# print(bob.name, bob.pay)                                # Fetch attached attibutes
# print(sue.name, sue.pay)                                # sue's & bob's attibutes differ


# Allow this file to be imported as well as run/tested
if __name__ == '__main__':                                  # When run for testing only
    # self test code
    bob = Person('Bob Smith')                               
    sue = Person('Sue Jones', job='dev', pay=100000)        
    print(bob.name, bob.pay)                                
    print(sue.name, sue.pay)


# Process embedded built-in types: strings, mutability
if __name__ == '__main__':
    bimri = Person('Bimri Codes')
    peres = Person('Peres Jones', job='writer', pay=100000)
    print(bimri.name, bimri.pay)
    print(peres.name, peres.pay)
    print(bimri.name.split()[:1])                           # Extract object's first name
    peres.pay *=1.10                                        # Give this object a raise
    print('%.2f' % peres.pay)


# Add methods to encapsulate operations for maintainability
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name 
        self.job  = job 
        self.pay  = pay
    def lastName(self):                                     # Behavior methods
        return self.name.split()[:1]                        # self is implied subject
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))            # Must change here only


if __name__ == '__main__':
    oluchi = Person('Oluchi Ibeneme')
    nyathi = Person('Pamela Nyathi', job='lab technician', pay=250000)
    print(oluchi.name, oluchi.pay)
    print(nyathi.name, nyathi.pay)
    print(nyathi.lastName(), oluchi.lastName())             # Use the new methods    
    nyathi.giveRaise(.10)                                   # instead of hardcoding
    print(nyathi.pay)



# Add __repr__ overload method for printing objects
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name 
        self.job  = job 
        self.pay  = pay
    def lastName(self):                                     
        return self.name.split()[:1]                        
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):                                     # Added method
        return '[Person: %s, %s]' % (self.name, self.pay)   # String to print
    

if __name__ == '__main__':
    oluchi = Person('Oluchi Ibeneme')
    nyathi = Person('Pamela Nyathi', job='lab technician', pay=250000)
    print(oluchi)
    print(nyathi)
    print(nyathi.lastName(), oluchi.lastName())             # Use the new methods    
    nyathi.giveRaise(.10)                                   # instead of hardcoding
    print(nyathi)


"Augmenting Methods: The Bad Way"
class Manager(Person):                                      # Define a subclass of Person                                  # Inherit Person attrs
    def giveRaise(self, percent, bonus=.10):                # Redefine to customize
        self.pay = int(self.pay * (1 + percent + bonus))    # Bad: cut and paste


"Augmenting Methods: The Good Way"
'''
This code leverages the fact that a class’s method can always be called either through
an instance (the usual way, where Python sends the instance to the self argument
automatically) or through the class (the less common scheme, where you must pass the
instance manually). In more symbolic terms, recall that a normal method call of this
form:
    instance.method(args...)

is automatically translated by Python into this equivalent form:
    class.method(instance, args...)
'''
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):                # Redefine at this level
        Person.giveRaise(self, percent + bonus)             # Call Person's version; Good: augment original


if __name__ == '__main__':
    oluchi = Person('Oluchi Ibeneme')
    nyathi = Person('Pamela Nyathi', job='lab technician', pay=250000)
    print(oluchi)
    print(nyathi)
    print(nyathi.lastName(), oluchi.lastName())             
    nyathi.giveRaise(.10)                                   
    print(nyathi)
    rio = Manager('Rio Je', 'mgr', 500000)                  # Make a Manager:__init__
    rio.giveRaise(.10)                                      # Runs custom version
    print(rio.lastName())
    print(rio)


'''
To test our Manager subclass customization, we’ve also added self-test code that makes
a Manager, calls its methods, and prints it. When we make a Manager, we pass in a name,
and an optional job and pay as before—because Manager had no __init__ constructor,
it inherits that in Person.
'''


"Polymorphism in Action"
if __name__ == '__main__':
    oluchi = Person('Oluchi Ibeneme')
    nyathi = Person('Pamela Nyathi', job='lab technician', pay=250000)
    print(oluchi)
    print(nyathi)
    print(nyathi.lastName(), oluchi.lastName())             
    nyathi.giveRaise(.10)                                   
    print(nyathi)
    rio = Manager('Rio Je', 'mgr', 500000)                  
    rio.giveRaise(.10)                                      
    print(rio.lastName())
    print(rio)
    print('--All three--')
    for obj in (oluchi, nyathi, rio):                                   # Process objects generically
        obj.giveRaise(.10)                                      # Run this object's giveRaise
        print(obj)
    


# Add customization of constructor in a subclass
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):                          # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)             # Run original with 'mgr'
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    oluchi = Person('Oluchi Ibeneme')
    nyathi = Person('Pamela Nyathi', job='lab technician', pay=250000)
    print(oluchi)
    print(nyathi)
    print(nyathi.lastName(), oluchi.lastName())             
    nyathi.giveRaise(.10)                                   
    print(nyathi)
    rio = Manager('Rio Je', 500000)                         # Job name not needed:
    rio.giveRaise(.10)                                      # Implied/set by class
    print(rio.lastName())
    print(rio)

    
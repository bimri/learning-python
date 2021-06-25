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


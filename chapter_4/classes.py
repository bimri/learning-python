'''
object-oriented programming in Python— an optional but powerful feature
of the language that cuts development time by supporting programming by customization
'''

# classes define new types
# of objects that extend the core set


class Worker:
    def __init__(self, name, pay):                # Initialize when created
        self.name = name                          # self is the new object
        self.pay  = pay 
    
    def lastName(self):
        return self.name.split()[-1]              # Split string on blanks
    
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)               # Update pay in place


bimri  = Worker('Bimri Kintu', 500000)            # Make two instances
unity = Worker('Unity Techi', 300000)             # Each has name and pay attrs

print(bimri.lastName())                           # call method: bimri is self
print(unity.lastName())

unity.giveRaise(.10)                              # Updates unity's pay
bimri.giveRaise(.1)

print(unity.pay)
print(bimri.pay)

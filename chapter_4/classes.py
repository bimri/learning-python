'''object-oriented programming in Python—an optional but powerful feature
of the language that cuts development time by supporting programming by customization'''

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
nyathi = Worker('Nyathi Nomuhle', 300000)         # Each has name and pay attrs

print(bimri.lastName())                           # call method: bimri is self
print(nyathi.lastName())

nyathi.giveRaise(.10)                             # Updates nyathi's pay
bimri.giveRaise(.1)

print(nyathi.pay)
print(bimri.pay)

"OOP and Inheritance: “Is-a” Relationships"
'''
From a programmer’s point of view, inheritance is kicked off by attribute qualifications, which
trigger searches for names in instances, their classes, and then any superclasses. From
a designer’s point of view, inheritance is a way to specify set membership: a class defines
a set of properties that may be inherited and customized by more specific sets (i.e.,
subclasses).
'''

class Employee:
    def __init__(self, name, salary=0):
        self.name = name 
        self.salary = salary 
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=50000)
    def work(self):
        print(self.name, "makes food")
    

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=40000)
    def work(self):
        print(self.name, "interfaces with customer")


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")
    

if __name__ == "__main__":
    bob = PizzaRobot('bob')             # Make a robot named bob
    print(bob)                          # Run inherited __repr__
    bob.work()                          # Run type-specific action
    bob.giveRaise(0.20)                 # Give bob a 20% raise
    print(bob); print()
    
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()

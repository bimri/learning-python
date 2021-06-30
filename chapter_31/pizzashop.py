"OOP and Composition: “Has-a” Relationships"
'''
From a programmer’s point of view, composition involves embedding other objects in a container
object, and activating them to implement container methods. To a designer,
composition is another way to represent relationships in a problem domain. But, rather
than set membership, composition has to do with components—parts of a whole.

Composition also reflects the relationships between parts, called “has-a” relationships.
Some OOP design texts refer to composition as aggregation, or distinguish between the
two terms by using aggregation to describe a weaker dependency between container
and contained. In this text, a “composition” simply refers to a collection of embedded
objects. The composite class generally provides an interface all its own and implements
it by directing the embedded objects.

As a rule of thumb, classes can represent just about
any objects and relationships you can express in a sentence; just replace nouns with
classes (e.g., Oven), and verbs with methods (e.g., bake), and you’ll have a first cut at a
design.
'''

from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name 
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)
    

class Oven:
    def bake(self):
        print("oven bakes")
    

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')                     # Embeded other objects
        self.chef   = PizzaRobot('Bob')                 # A robot named bob
        self.oven   = Oven()

    def order(self, name):
        customer = Customer(name)                       # activate other objects
        customer.order(self.server)                     # Customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
    

if __name__ == "__main__":
    scene = PizzaShop()                     # Make the composite
    scene.order('Homer')                    # Simulate Homer's order
    print('...')
    scene.order('Shaggy')                   # Simulate Shaggy's order

""" 
The Dead Parrot Sketch. Consider the object embedding structure captured in
Figure 32-2.

Code a set of Python classes to implement this structure with composition. Code
your Scene object to define an action method, and embed instances of the Cus
tomer, Clerk, and Parrot classes (each of which should define a line method that
prints a unique message). The embedded objects may either inherit from a common
superclass that defines line and simply provide message text, or define line themselves.
In the end, your classes should operate like this:
    % python
    >>> import parrot
    >>> parrot.Scene().action()         # Activate nested objects
    customer: "that's one ex-bird!"
    clerk: "no it isn't..."
    parrot: None 

""" 
class Actor:
    def line(self): 
        print(self.name + ':', repr(self.says()))

class Customer(Actor):
    name = 'customer'
    def says(self): 
        return "that's one ex-bird!"

class Clerk(Actor):
    name = 'clerk'
    def says(self): 
        return "no it isn't..."

class Parrot(Actor):
    name = 'parrot'
    def says(self): 
        return None

class Scene:
    def __init__(self):
        self.clerk = Clerk()                                        # Embed some instances
        self.customer = Customer()                                  # Scene is a composite
        self.subject = Parrot()
    def action(self):
        self.customer.line()                                        # Delegate to embedded
        self.clerk.line()
        self.subject.line()


if __name__ == "__main__":
    Scene().action()

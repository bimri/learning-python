"Customization: Same-argument constraints"

class Employee:
    def __init__(self, name, salary):                               # Common superclass
        self.name = name
        self.salary = salary
    
class Chef1(Employee):
    def __init__(self, name):                                       # Differing arguments
        Employee.__init__(self, name, 50000)                        # Dispatch by direct call
    

class Server1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    

if __name__ == "__main__":
    bob = Chef1('Bob')
    sue = Server1('Sue')
    print(bob.salary, sue.salary)


class Chef2(Employee):
    def __init__(self, name):       
        super().__init__(name, 50000)                               # Dispatch by super()


class Server2(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)


if __name__ == "__main__":
    print()
    bob = Chef2('Bob')
    sue = Server2('Sue')
    print(bob.salary, sue.salary)


""" 
Watch what happens, though, when an employee is a member of both categories. Because
the constructors in the tree have differing argument lists, we’re in trouble:
""" 
class TwoJobs(Chef2, Server2): pass

if __name__ == "__main__":
    print()
    # tom = TwoJobs('Tom')            # TypeError: __init__() takes 2 positional arguments but 3 were given
    print(TwoJobs.__mro__)
    print(Chef2.__mro__)

    """ 
    By contrast, the direct by-name call scheme still works when the classes are mixed,
    though the results are a bit dubious—the combined category gets the pay of the leftmost
    superclass:
    """ 
    class TwoJobs(Chef1, Server1): pass

    tom = TwoJobs('Tom')
    print(tom.salary)

    class TwoJobs(Chef1, Server1):
        def __init__(self, name): Employee.__init__(self, name, 70000)

    tom = TwoJobs('Tom')
    print(tom.salary)


    class TwoJobs(Chef2, Server2):
        def __init__(self, name): super().__init__(name, 70000)
    
    tom = TwoJobs('Tom')                            # TypeError: __init__() takes 2 positional arguments but 3 were given
    
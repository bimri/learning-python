# Embedding-based Manager alternative
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
    

class Manager:
    '''
    this Manager alternative is representative of a general coding
    pattern usually known as delegation—a composite-based structure that manages a
    wrapped object and propagates method calls to it.
    '''
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)                  # Embeded a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)                  # Intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr)                       # Delegate all other attrs
    def __repr__(self):
        return str(self.person)                                 # Must ovreload again (in 3.X)
    

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


"Example: Adding Methods to Classes"
'Manual Augmentation'
# Extend manually - adding new methods to classes

class Client1:
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2


class Client2:
    value = 'ni?'
    def eggsfunc(obj):
        return obj.value * 4
    def hamfunc(obj, value):
        return value + 'ham'


Client1.eggs = eggsfunc
Client1.ham = hamfunc

Client2.eggs = eggsfunc
Client2.ham = hamfunc

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


'''
methods can always be assigned to a class after it’s been created,
as long as the methods assigned are functions with an extra first argument to receive
the subject self instance—this argument can be used to access state information accessible
from the class instance, even though the function is defined independently of
the class.
'''


"""
This scheme works well in isolated cases and can be used to fill out a class arbitrarily
at runtime. It suffers from a potentially major downside, though: we have to repeat the
augmentation code for every class that needs these methods. In our case, it wasn’t too
onerous to add the two methods to both classes, but in more complex scenarios this
approach can be time-consuming and error-prone.
"""

"Scope: An all-or-nothing model"
'''
Also keep in mind that traditional classes that were not written to use super in this role
cannot be directly used in such cooperative dispatch trees, as they will not forward calls
along the MRO chain. It’s possible to incorporate such classes with proxies that wrap
the original object and add the requisite super calls, but this imposes both additional
coding requirements and performance costs on the model. Given that there are many
millions of lines of existing Python code that do not use super, this seems a major
detriment.
'''

class B:
    def __init__(self): print('B.__init__'); super().__init__()

class C:
    def __init__(self): print('C.__init__'); super().__init__()

class D(B, C):
    def __init__(self): print('D.__init__'); super().__init__()


if __name__ == '__main__':
    X = D()
    print(D.__mro__)


# What if you must use a class that doesn't call super?
class B:
    def __init__(self): print('B.__init__')

class D(B, C):
    def __init__(self): print('D.__init__'); super().__init__()


if __name__ == '__main__':
    print()
    X = D()                     # It's an all-or-nothing tool...

'''
Satisfying this mandatory propagation requirement may be no simpler than direct byname
calls—which you might still forget, but which you won’t need to require of all
the code your classes employ.
'''

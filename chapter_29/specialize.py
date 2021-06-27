"Class Interface Techniques"
# Extension is only one way to interface with a superclass.
'''
a variety of common techniques:
- Super
    Defines a method function and a delegate that expects an action in a subclass.

- Inheritor
    Doesn’t provide any new names, so it gets everything defined in Super.

- Replacer
    Overrides Super’s method with a version of its own.

- Extender
    Customizes Super’s method by overriding and calling back to run the default.

- Provider
    Implements the action method expected by Super’s delegate method.
'''
class Super:
    def method(self):
        print('in Super.method')                                    # Default behavior
    def delegate(self):
        self.action()                                               # Expected to be defined
    

class Inheritor(Super):                                             # Inherit method verbatim
    pass


class Replacer(Super):                                              # Replace method completely
    def method(self):
        print('in Replacer.method')
    

class Extender(Super):                                              # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')
    

class Provider(Super):                                              # Fill in a required method
    def action(self):
        print('in Provider.action')

    
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()


'''
When we call the delegate method through a Provider instance, two independent inheritance
searches occur:
    1. On the initial x.delegate call, Python finds the delegate method in Super by
    searching the Provider instance and above. The instance x is passed into the
    method’s self argument as usual.

    2. Inside the Super.delegate method, self.action invokes a new, independent inheritance
    search of self and above. Because self references a Provider instance,
    the action method is located in the Provider subclass.

At least in terms of the delegate method, the superclass in this example is what is
sometimes called an abstract superclass—a class that expects parts of its behavior to be
provided by its subclasses. If an expected method is not defined in a subclass, Python
raises an undefined name exception when the inheritance search fails.

Class coders sometimes make such subclass requirements more obvious with assert
statements, or by raising the built-in NotImplementedError exception with raise statements.

    class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined!'             # If this version is called
    
    >>> X = Super()
    >>> X.delegate()
    AssertionError: action must be defined!



Alternatively, some classes simply raise a NotImplemen
tedError exception directly in such method stubs to signal the mistake:
    class Super:
        def delegate(self):
            self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')
    
    >>> X = Super()
    >>> X.delegate()
    NotImplementedError: action must be defined!
'''


"""
For instances of subclasses, we still get the exception unless the subclass provides the
expected method to replace the default in the superclass:
    >>> class Sub(Super): pass
    
    >>> X = Sub()
    >>> X.delegate()
    NotImplementedError: action must be defined!
    
    >>> class Sub(Super):
            def action(self): print('spam')
    
    >>> X = Sub()
    >>> X.delegate()
    spam

"""
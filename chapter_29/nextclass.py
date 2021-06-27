class NextClass:                                        # Define class
    def printer(self, text):                            # Define method
        self.message = text                             # Change instance
        print(self.message)                             # Access instance
    

x = NextClass()                                         # Make instance
x.printer('instance call')                              # Call its method

print(x.message)                                        # Instance changed


'''
methods may be called in one of two ways—through an instance,
or through the class itself.

Calls routed through the instance and the class have the exact same effect, as long as
we pass the same instance object ourselves in the class form.

    >>> NextClass.printer('bad call')
    TypeError: unbound method printer() must be called with NextClass instance...
'''
NextClass.printer(x, 'class call')                      # Direct class call
print(x.message)                                        # Instance changed again

'''
Function-related statements and expressions
        Statement or expression                                         Examples

Call expressions                                        myfunc('spam', 'eggs', meat=ham, *rest)

def                                                     def printer(messge):
                                                            print('Hello ' + message)

return                                                  def adder(a, b=1, *c):
                                                                return a + b + c[0]

global                                                  x = 'old'
                                                        def changer():
                                                            global x; x = 'new'

nonlocal (3.X)                                          def outer():
                                                            x = 'old'
                                                            def changer():
                                                                nonlocal x; x = 'new'

yield                                                   def squares(x):
                                                            for i in range(x): yield i ** 2

lambda       



Generic format for functions:
    def name(arg1, arg2,... argN):
        statements
                                           funcs = [lambda x: x**2, lambda x: x**3]
'''


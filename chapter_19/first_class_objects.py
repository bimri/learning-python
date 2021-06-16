"Indirect Function Calls"
# functions belong to the same
# general category as other objects

'first-class object model'
# functions must be treated as data
def echo(message):                          # Name echo assigned to function object
    print(message)

echo('Direct Call')                         # Call object through original name

x = echo                                    # Now x references the function too

x('Indirect call!')                         # Call object through name by adding()


"Pass functions to other functions as arguments"
def indirect(func, arg):
    func(arg)                                               # Call the passed-in object by adding ()

indirect(echo, 'Argument call Bimri!')                      # Pass the function to another function


'''
You can even stuff function objects into data structures, 
as though they were integers or strings
'''
schedule = [ (echo, 'AMAPIANO!'), (echo, 'SOUTH AFRICA') ]

for (func, arg) in schedule:
    func(arg)                                               # Call functions embedded in containers


"functions can also be created and returned for use elsewhere"
def make(label):                                            # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Purple')                                          # Label in enclosing scope is retained
F('Color!')                                                 # Call the functin that make returned  
F('Rainbow!')


'''
Python’s universal first-class object model and lack of 
type declarations make for an incredibly flexible 
programming language.
'''
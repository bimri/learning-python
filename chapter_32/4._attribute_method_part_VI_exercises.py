""" 
4. Attribute methods. Write a class called Attrs with methods that intercept every
attribute qualification (both fetches and assignments), and print messages listing
their arguments to stdout. Create an Attrs instance, and experiment with qualifying
it interactively. What happens when you try to use the instance in expressions?
Try adding, indexing, and slicing the instance of your class.
"""

class Attrs:
    def __getattr__(self, name):
        print('get %s' % name)
    
    def __setattr__(self, name, value):
        print('set %s %s' % (name, value))
    

if __name__ == '__main__':
    a = Attrs()
    a.x
    a.x = 1
    a.append


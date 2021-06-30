"Object Destruction: __del__"
'''
__init__ constructor is called whenever an instance is generated
the destructor method __del__, is run automatically when an instance’s space is being reclaimed
(i.e., at “garbage collection” time):
'''
class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name
    def live(self):
        print(self.name)
    def __del__(self):
        print('Goodbye ' + self.name)


if __name__ == "__main__":
    brian = Life('Brian')
    brian.live()

    brian = 'loretta'


"""
Here, when brian is assigned a string, we lose the last reference to the Life instance
and so trigger its destructor method. This works, and it may be useful for implementing
some cleanup activities, such as terminating a server connection. However, destructors
are not as commonly used in Python as in some OOP languages
"""

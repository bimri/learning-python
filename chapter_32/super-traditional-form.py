"Traditional Superclass Call Form: Portable, General"

class C:                                                            # In Python 2.X and 3.X
    def act(self):
        print('spam')


class D(C):
    def act(self):
            C.act(self)                                             # Name superclass explicitly, pass self
            print('eggs')


if __name__ == '__main__':
    x = D()
    x.act()

"Customization: Method replacement"
'''
On a related note, the universal deployment expectations of super may make it difficult
for a single class to replace (override) an inherited method altogether. Not passing the
call higher with super—intentionally in this case—works fine for the class itself, but
may break the call chain of trees it’s mixed into, thereby preventing methods elsewhere
in the tree from running.
'''
class A:
    def method(self): print('A.method'); super().method()

class B(A):
    def method(self): print('B.method'); super().method()

class C:
    def method(self): print('C.method')                                 # No super: must anchor the chain!

class D(B, C):
    def method(self): print('D.method'); super().method()


if __name__ == "__main__":
    d = D()
    d.method()


# What if a class needs to replace a super's default entirely?
class B(A):
    def method(self): print('B.method')                                 # Drop super to replace A's method

class D(B, C):
    def method(self): print('D.method'); super().method()


if __name__ == "__main__":
    print()
    d = D()
    d.method()                  # But replacement also breaks the call chain...


class D(B, C):
    def method(self): print('D.method'); B.method(self); C.method(self)


if __name__ == "__main__":
    print()
    D().method()
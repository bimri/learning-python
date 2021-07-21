"Coupling: Application to mix-in classes"
'''
Subtly, when we say super selects the next class in the MRO, we really mean the next
class in the MRO that implements the requested method—it technically skips ahead until
it finds a class with the requested name.
'''
# Mix-ins work for disjoint method sets

class A:
    def other(self): print('A.other')

class Mixin(A):
    def other(self): print('Mixin.other'); super().other()

class B:
    def method(self): print('B.method')

class C(Mixin, B):
    def method(self): print('C.method'); super().other(); super().method()

class C(B, Mixin):
    def method(self): print('C.method'); super().other(); super().method()

# But direct calls work here too: explicit is better than implicit
class C(Mixin, B):
    def method(self): print('C.method'); Mixin.other(self); B.method(self)


if __name__ == '__main__':
    C().method()
    print(C.__mro__)
    
    print()
    print('-' * 100)
    print(C.__mro__)

    X = C()
    X.method()


# But for nondisjoint methods: super creates overly strong coupling
class A:
    def method(self): print('A.method')


class Mixin(A):
    def method(self): print('Mixin.method'); super().method()

class B(A):
    def method(self): print('B.method')                             # super here would invoke A after B

class C(Mixin, B):
    def method(self): print('C.method'); super().method()


if __name__ == '__main__':
    print()
    print('-' * 100)
    Mixin().method()

    print()
    C().method()



# And direct calls do not: they are immune to context of use
class A:
    def method(self): print('A.method')

class Mixin(A):
    def method(self): print('Mixin.method'); A.method(self) # C irrelevant

class C(Mixin, B):
    def method(self): print('C.method'); Mixin.method(self)


if __name__ == '__main__':
    print()
    print('-' * 100)
    C().method()
    
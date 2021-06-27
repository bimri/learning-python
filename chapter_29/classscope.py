'''
Though they are normally coded at the top level of a module, classes also sometimes
appear nested in functions that generate them—a variation on the “factory function”
(a.k.a. closure), with similar state retention roles


Although classes have access to enclosing functions’ scopes, though, they do not act
as enclosing scopes to code nested within the class: Python searches enclosing functions
for referenced names, but never any enclosing classes. That is, a class is a local scope
and has access to enclosing local scopes, but it does not serve as an enclosing local scope
to further nested code. Because the search for names used in method functions skips
the enclosing class, class attributes must be fetched as object attributes using inheritance.
'''
X = 1

def nester():
    print(X)                                        # Global: 1
    class C:
        print(X)                                    # Global: 1
        def method1(self):
            print(X)                                # Global: 1
        def method2(self):
            X = 3                                   # Hides global
            print(X)                                # Local: 3
    
    I = C()
    I.method1()
    I.method2()

print(X)                                            # Global: 1
nester()                                            # Rest: 1, 1, 1, 3
print('-'*40)


"""
Watch what happens, though, when we reassign the same name in nested function
layers: the redefinitions of X create locals that hide those in enclosing scopes, just as for
simple nested functions; the enclosing class layer does not change this rule, and in fact
is irrelevant to it:
"""
X = 1

def nester():
    X = 2                                               # Hides global
    print(X)                                            # Local: 2
    class C:
        print(X)                                        # In enclosing def (nester): 2
        def method1(self):
            print(X)                                    # In enclosing def (nester): 2
        def method2(self):
            X = 3                                       # Hides enclosing (nester)
            print(X)                                    # Local: 3

    I = C()
    I.method1()
    I.method2()

print(X)                                                # Global: 1
nester()                                                # Rest: 2, 2, 2, 3
print('-'*40)


'''
And here’s what happens when we reassign the same name at multiple stops along the
way: assignments in the local scopes of both functions and classes hide globals or enclosing
function locals of the same name, regardless of the nesting involved:
'''
X = 1

def nester():
    X = 2                                               # Hides global
    print(X)                                            # Local: 2
    class C:
        X = 3                                           # Class local hides nester's: C.X or I.X (not scoped)
        print(X)                                        # Local: 3
        def method1(self):
            print(X)                                    # In enclosing def (not 3 in class!): 2
            print(self.X)                               # Inherited class local: 3
        def method2(self):
            X = 4                                       # Hides enclosing (nester, not class)                        # Hides enclosing (nester)
            print(X)                                    # Local: 4
            self.X = 5                                  # Hides class
            print(self.X)                               # Located in instance: 5

    I = C()
    I.method1()
    I.method2()

print(X)                                                # Global: 1
nester()                                                # Rest: 2, 3, 2, 3, 4, 5
print('-'*40)
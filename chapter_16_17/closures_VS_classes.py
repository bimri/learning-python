"Retaining Enclosing Scope State with Defaults"
def f1():
    x = 88
    def f2(x=x):                                    # Remember enclosing scope X with defaults
        print(x)
    f2()

f1()                                                # Prints 88


'''
Code inside a def is never evaluated until the function is
actually called:'''
def f1():
    x = 88                                          # Pass x along instead of nesting
    f2(x)

def f2(x):
    print(x)

f1()


"Nested scopes, defaults, and lambdas"
# variation on the factory we saw earlier
def func():
    x = 4
    action = (lambda n: x ** n)                     # x remembered form enclosing def
    return action

x = func()
print(x(2))                                         # Prints 16, 4 ** 2


"programmers used defaults to pass values from an enclosing scope into lambdas, just as for defs"
def func():
    x = 4
    action = (lambda n, x=x: x ** n)                # Pass x in manually
    return action



"Loop variables may require defaults, not scopes"
def makeActions():
    acts = []
    for i in range(5):                              # Tries to rem each i
        acts.append(lambda x:i ** x)                # But all rem same last i!
    return acts

acts = makeActions()
print(acts[0])                          # doesn’t quite work

print(acts[0](2))                                   # All are 4 ** 2, 4 = value of last i
print(acts[1](2))                                   # This should be 1 ** 2 (1)
print(acts[2](2))                                   # This should be 2 ** 2 (4)
print(acts[4](2))                                   # ONLY this should be 4 ** 2 (16)


'''
Because defaults are evaluated when the nested function is created (not when
it’s later called), each remembers its own value for i:
'''
def makeActions():
    acts = []
    for i in range(5):                              # Use defaults instead
        acts.append(lambda x, i=i: i ** x)          # Rem current i
    return acts

acts = makeActions()
print(acts[0](2))                                  # 0 ** 2
print(acts[1](2))                                  # 1 ** 2                 # 0 ** 2
print(acts[2](2))                                  # 2 ** 2
print(acts[4](2))                                  # 4 ** 2


"Arbitrary scope nesting"
def f1():
    x = 99
    def f2():
        def f3():
            print(x)                                # Found in f1's local scope!
        f3()
    f2()

f1()

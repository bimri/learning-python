"Classes versus generators"
'''
Unlike classes, generator functions and expressions implicitly save their state and create
the methods required to conform to the iteration protocol—with obvious advantages
in code conciseness for simpler examples like these. On the other hand, the class’s more
explicit attributes and methods, extra structure, inheritance hierarchies, and support
for multiple behaviors may be better suited for richer use cases.
'''
def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2
    
def tester():
    for i in gsquares(1, 5):
        print(i, end=' ')

    print()
    # best and fastest way to accomplish a task in Python is often also the simplest:
    for i in (x ** 2 for x in range(1, 6)):
        print(i, end=' ')

    print()
    print([x ** 2 for x in range(1, 6)])

if __name__ == '__main__':
    tester()


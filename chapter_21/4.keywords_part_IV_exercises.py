def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly

print(adder())
print(adder(9))
print(adder(1, 2))
print(adder(34, 5, 32))
print(adder(ugly=1, good=2, bad=3))


# Second part solutions
def adder1(*args):                                                                  # Sum any number of positional args
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder2(**args):                                                                 # Sum any number of keyword args
    argskeys = list(args.keys())                                                    # list needed in 3.X!
    tot = args[argskeys[0]]
    for key in argskeys[1:]:
        tot += args[key]
    return tot

def adder3(**args):                                                                 # Same, but convert to list of values
    args = list(args.values())                                                      # list needed to index in 3.X!
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder4(**args):                                                                 # Same, but reuse positional version
    return adder1(*args.values())

print(adder1(1, 2, 3), adder1('aa', 'bb', 'cc'))
print(adder2(a=1, b=2, c=3), adder2(a='aa', b='bb', c='cc'))
print(adder3(a=1, b=2, c=3), adder3(a='aa', b='bb', c='cc'))
print(adder4(a=1, b=2, c=3), adder4(a='aa', b='bb', c='cc'))

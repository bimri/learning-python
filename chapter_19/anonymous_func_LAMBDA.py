"This expression creates a function to be called later"
"But, it returns the function instead of assigning it to a name"
'hence why they are called - "Anonymous(i.e. unnamed) functions"'

# in practice, used to inline a function definition
# or, defer execution of a piece of code


'''
lambda Basics:
    lambda argument1, argument2, argument3,... argumentN : expression using arguments
- is an expression lambda
- lambda is designed for coding simple functions, and def handles larger tasks.
'''
def func(x, y, z): return x + y + z
print(func(2, 3, 4))

# achieve the same effect with a lambda expression
f = lambda x, y, z: x + y + z
print(f(20, 30, 40))


"Defaults work on lambda arguments, just like in a def"
x = (lambda a='fee', b='fie', c='foe': a + b + c)
print(x("wee"))
print(x("wee", 'woo'))
print(x('wee', 'wzz', 'waa'))


"LEGB rule"
def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)                # Title in enclosing def scope
    return action

act = knights()
msg = act('robin')                                      # 'robin' passed to x

print(msg)
print(act)                                              # act: a function, not its result


"Scopes: lambdas Can Be Nested Too"
# lambdas are the main beneficies of nested function
#  scope lookup('E' in LEGB)
def action(x):
    return (lambda y: x + y)                            # Make & return function, remember x

act = action(99)
print(act)

print(act(2))                                                  # Call what action returned


'''
lambda also has access to the names in any enclosing lambda
'''
# nested lambda structure makes a function that makes a 
# function when called
action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))

print(
    ((lambda x: (lambda y: x + y))(99))(4)
)

"interest of readability, nested lambdas are generally best avoided"

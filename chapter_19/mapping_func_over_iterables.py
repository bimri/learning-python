"apply an operation to each item and collect the results"
# selecting columns in database tables, incrementing pay
# fields of employees in a company, parsing email attachments


'updating all the counters in a list can be done easily with a for loop'
counters = [1, 2, 3, 4]
updated = []

for x in counters:
    updated.append(x + 10)                  # Add 10 to each item

print(updated)


"Map function applies a passed-in function to each item in an"
"iterable object and return a list containing all the function call results"
def inc(x):
    return x + 10                           # Function to be run

# is an iterable map, so a list call is used to force it to produce all its results.
print(
    list(map(inc, counters))                # Collect results
)

'''
Because map expects a function to be passed in and applied, 
it also happens to be one of the places where lambda commonly 
appears:
'''
print(
    list(map((lambda x: x + 3), counters))    # Function expression
)

# general mapping utility
def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

print(
    list(map(inc, [1, 2, 3]))                   # Built-in us an iterable
)

print(
    mymap(inc, [1, 2, 3])                       # Ours builds a list
)


# Advance use case for Map
print(pow(3, 4))                                # 3**4
print(
    list(map(pow, [1,2,3], [2,3,4]))            # 1**2, 2**3, 3**4
)


# Similarity of map & comprehension expressions
print(
    list(map(inc, [12, 13, 45, 89]))
)

print(
    [inc(x) for x in [12, 13, 45, 89]]          # Use () parens to generate items instead
)


'''
map may be faster to run than a list comprehension (e.g., when mapping
a built-in function), and it may also require less coding

On the other hand, because map applies a function call to each item instead of an arbitrary expression, it is a somewhat
less general tool, and often requires extra helper functions or lambdas

wrapping a comprehension in parentheses instead of square brackets creates an object that
generates values on request to save memory and increase responsiveness
'''

import sys 

print(
    sys.__doc__                                             # human-readable description of a built-in module
)

# Functions, classes, and methods within built-in modules have attached descriptions
print(
    sys.getrefcount.__doc__
)

# Read built-in functions via docstrings
print(
    int.__doc__
)

print(
    map.__doc__
)
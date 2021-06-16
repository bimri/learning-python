"Definitions and Calls"
# Two sides to the function picture: a definition(def creates the function)
# and a call(expression that tells Python to run the func's body)

def times(x, y):                            # Creates and assigns function
    return x * y                            # Body executed when called


print(times(10**10, 6))                     # Arguments in parentheses
print(times(67, 89))

x = times(3.14, 4)                          # Save the result object
print(x)

print(
    times('Cherono', 3)                     # Functions are "typeless"         
)


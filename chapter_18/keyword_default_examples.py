def f(a, b, c): print(a, b, c)

#MUST call with all three arguments defined at func header
f(1, 3, 4)


"Keywords"
f(c=3, b=2, a=1)

# a gets 1 by position, b and c passed by name
f(1, c=3, b=2)


"Defaults"
def f(a, b=2, c=3): print(a, b, c)                  # a required, b & c are optional

# Use defaults
f(1)
f(a=10)

# Override defaults
f(1, 4)
f(1, 4, 5)

# Choose defaults
f(1, c=6)


"Combining keywords and defaults"
# First 2 required
def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))

func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)

'''
keep in mind that the form name=value means different things in the 
call and the def: a keyword in the call and a default in the header
'''

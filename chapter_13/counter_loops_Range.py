# Loop-related function
# used most often to generate indexes in a for
# you can use it anywhere you need a series of integers
''' Range is an iterable that generates items
range on demand''' 

print(
    list(range(5)),
    list(range(2, 5)),
    list(range(0, 10, 2))
)

'''Ranges can also be nonpositive
and nonascending'''

print(
    list(range(-5, 5)),
    list(range(5, -5, -1))
)


# provide a simple way to repeat an action
# a specific number of times
for i in range(3):
    print(i, 'Pythons')

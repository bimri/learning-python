reply = """
        Greetings...
        Hello %(name)s!
        Your age is %(age)s
        """

values = {'name': 'Bob', 'age': 40}
print(reply % values)


food = 'spam'
qty = 10
# print(vars())
print('%(qty)d more %(food)s' % vars())



'Formatting Method Basics'
template = '{0}, {1} and {2}'                                               # By position
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'                                     # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'                                        # By Both
print(template.format('ham', motto='spam', food='eggs'))

template = '{}, {} and {}'                                                  # By relative position
print(template.format('spam', 'ham', 'eggs'))

# Expression
template = '%s, %s and %s'
print(template % ('spam', 'ham', 'eggs'))

template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))


print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))
X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(X)

print(X.split(' and '))

Y = X.replace('and', 'but under no circumstances')
print(Y)

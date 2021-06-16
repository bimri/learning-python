print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'} )


reply = '''                                         
Greetings...
Hello %(name)s!
Your age is %(age)s
'''

values = {'name': 'Bimri', 'age': 4000}             # Build up values to substitute
print(reply % values)                               # Perform substitutions    


food = 'spam'
qty = 10

print(vars())
print()
print('%(qty)d more %(food)s' % vars())

'''If you really want to store native Python objects, but you can’t trust
the source of the data in the file, Python’s standard library pickle module is ideal.'''
import pickle


D = {'a': 1, 'b': 2}

F = open('pckl.txt', 'wb')
pickle.dump(D, F)                           # pickle any object to file
F.close()


F = open('pckl.txt', 'rb')
E = pickle.load(F)
print(E)

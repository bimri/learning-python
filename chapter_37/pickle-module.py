"The pickle Object Serialization Module"
'''
the pickle module always creates a
bytes object, regardless of the default or passed-in “protocol” (data format level).
'''
import pickle                                   # dumps() returns pickle string

print(pickle.dumps([1, 2, 3]))                  # Python 3.X default protocol=3=binary              
print(pickle.dumps([1, 2, 3], protocol=0))      # ASCII protocol 0, but still bytes


"""
This implies that files used to store pickled objects must always be opened in binary
mode in Python 3.X, since text files use str strings to represent data, not bytes—the
dump call simply attempts to write the pickle string to an open output file:
    >>> pickle.dump([1, 2, 3], open('temp', 'w')) # Text files fail on bytes!
    TypeError: must be str, not bytes # Despite protocol value
    
    >>> pickle.dump([1, 2, 3], open('temp', 'w'), protocol=0)
    TypeError: must be str, not bytes
    
    >>> pickle.dump([1, 2, 3], open('temp', 'wb')) # Always use binary in 3.X
    
    >>> open('temp', 'r').read() # This works, but just by luck
    '\u20ac\x03]q\x00(K\x01K\x02K\x03e.'
"""


'''
Notice the last result here didn’t issue an error in text mode only because the stored
binary data was compatible with the Windows platform’s UTF-8 default decoder; this
was really just luck (and in fact, this command failed when printing in older Pythons,
and may fail on other platforms). Because pickle data is not generally decodable Unicode
text, the same rule holds on input—correct usage in 3.X requires always both
writing and reading pickle data in binary modes, whether unpickling or not:
'''
pickle.dump([1, 2, 3], open('temp', 'wb'))
print(pickle.load(open('temp', 'rb')))
print(open('temp', 'rb').read())


'''
If you care about version neutrality, though, or don’t want to care about protocols or
their version-specific defaults, always use binary-mode files for pickled data—the following
works the same in Python 3.X and 2.X:
'''
import pickle
pickle.dump([1, 2, 3], open('temp', 'wb'))                  # Version neutral
print(
    pickle.load(open('temp', 'rb')) # And required in 3.X
)
    
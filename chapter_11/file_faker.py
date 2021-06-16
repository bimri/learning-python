import sys


class FileFaker:
    def write(self, string):
        pass                    # Do something with printed text in string


sys.stdout = FileFaker()
print('someObjects')            # Sends to class write method


# Redirection - to interface - method
myobj = FileFaker()                             # Redirect to object for one print
print('someObjects', file=myobj)                # Does not reset sys.stdout    

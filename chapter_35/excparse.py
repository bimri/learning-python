"Providing Exception Methods"
'''
Besides enabling application-specific state information, custom constructors also better
support extra behavior for exception objects. That is, the exception class can also define
methods to be called in the handler.
'''
class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.file, self.line, file=log)


def parser():
    raise FormatError(40, 'spam.txt') 


if __name__ == "__main__":
    try:
        parser()
    except FormatError as exc:
        exc.logerror()

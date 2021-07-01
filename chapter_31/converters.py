from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()
    

if __name__ == "__main__":
    import sys 
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process(); print()

    class HTMLize:
        """
        we get both uppercase conversion (by inheritance) and HTML formatting (by composition), even though the
        core processing logic in the original Processor superclass knows nothing about either step. 
        """
        def write(self, line):
            print('<PRE>%s</PRE>' % line.rstrip())
    
    print(Uppercase(open('trispam.txt'), HTMLize()).process())
    
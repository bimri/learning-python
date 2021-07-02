#!python
"Listing instance attributes with __dict__"

class ListIntance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; displays instance attrs only; self is
    instance of lowest class; __X names avoid clashing with client's attrs
    """
    def __attrnames(self):
        """
        pseudoprivate naming pattern for its worker method: __attrnames. As
        we learned earlier in this chapter, Python automatically localizes any such name
        to its enclosing class by expanding the attribute name to include the class name (in
        this case, it becomes _ListInstance__attrnames).
        """
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    # generator
    # def __attrnames(self):
    #     return ''.join('\t%s=%s\n' % (attr, self.__dict__ [attr])
    #                         for attr in sorted(self.__dict__))
    
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                            self.__class__.__name__,             # My class's name
                            id(self),                           # My address
                            self.__attrnames())                 # name=value list


if __name__ == '__main__':
    class Spam(ListIntance):
        def __init__(self):
            self.data1 = 'food'
        
    x = Spam()
    print(x)


    display = str(x)
    print(display)
    print(x)
                                      
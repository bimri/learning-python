"Stream Processors Revisited"
# def processor(reader, converter, writer):
#     while True:
#         data = reader.read()
#         if not data: break 
#         data = converter(data)
#         writer.write(data)


'''
Rather than using a simple function here, we might code this as a class that uses composition
to do its work in order to provide more structure and support inheritance.
'''
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader 
        self.writer = writer 
    
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break 
            data = self.converter(data)
            self.writer.write(data)
        
    def converter(self, data):
        """
        converter method that it expects subclasses to fill in
        it’s an example of the abstract superclass model
        """
        assert False, 'converter must be defined'                       # Or raise exception
    


"""
Coded this way, reader and writer objects
are embedded within the class instance (composition), and we supply the conversion
logic in a subclass rather than passing in a converter function (inheritance).
"""

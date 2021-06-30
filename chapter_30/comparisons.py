"""
These methods are generally straightforward to use, but keep the following
qualifications in mind:
    • Unlike the __add__/__radd__ pairings, there are no right-side variants
    of comparison methods. Instead, reflective methods are used when only one
    operand supports comparison (e.g., __lt__ and __gt__ are each other’s reflection).
    
    • There are no implicit relationships among the comparison operators. The truth of
    == does not imply that != is false, for example, so both __eq__ and __ne__ should
    be defined to ensure that both operators behave correctly.

"""
class C:
    data = 'spam'
    def __gt__(self, other):                            # 3.X and 2.X version
        return self.data > other
    def __lt__(self, other):
        return self.data < other
   
if __name__ == "__main__":
    X = C()
    print(X > 'ham')            # True (runs __gt__)
    print(X < 'ham')            # False (runs __lt__)

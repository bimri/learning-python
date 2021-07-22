""" 
Zoo animal hierarchy. Consider the class tree shown in Figure 32-1.
Code a set of six class statements to model this taxonomy with Python inheritance.
Then, add a speak method to each of your classes that prints a unique message,
and a reply method in your top-level Animal superclass that simply calls
self.speak to invoke the category-specific message printer in a subclass below (this
will kick off an independent inheritance search from self). Finally, remove the
speak method from your Hacker class so that it picks up the default above it. When
you’re finished, your classes should work this way:
""" 
class Animal:
    def reply(self): self.speak()                                                               # Back to subclass
    def speak(self): print('spam')                                                              # Custom message

class Mammal(Animal):
    def speak(self): print('huh?')

class Cat(Mammal):
    def speak(self): print('meow')

class Dog(Mammal):
    def speak(self): print('bark')

class Primate(Mammal):
    def speak(self): print('Hello world!')

class Hacker(Primate): pass                                                                     # Inherit from Primate


if __name__ == "__main__":
    for a in (Animal(), Mammal(), Cat(), Dog(), Primate(), Hacker()):
        a.reply()
        # a.speak()
        print()

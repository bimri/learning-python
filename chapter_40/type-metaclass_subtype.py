"Metaclasses Are Subclasses of Type"
'''
Why would we care that classes are instances of a type class in 3.X? It turns out that
this is the hook that allows us to code metaclasses. Because the notion of type is the
same as class today, we can subclass type with normal object-oriented techniques and
class syntax to customize it. And because classes are really instances of the type class,

creating classes from customized subclasses of type allows us to implement custom
kinds of classes. In full detail, this all works out quite naturally—in 3.X, and in 2.X
new-style classes:
• type is a class that generates user-defined classes.
• Metaclasses are subclasses of the type class.
• Class objects are instances of the type class, or a subclass thereof.
• Instance objects are generated from a class.

In other words, to control the way classes are created and augment their behavior, all
we need to do is specify that a user-defined class be created from a user-defined metaclass
instead of the normal type class.

Notice that this type instance relationship is not quite the same as normal inheritance.
User-defined classes may also have superclasses from which they and their instances
inherit attributes as usual. As we’ve seen, inheritance superclasses are listed in parentheses
in the class statement and show up in a class’s __bases__ tuple. The type from
which a class is created, though, and of which it is an instance, is a different relationship.

Inheritance searches instance and class namespace dictionaries, but classes may also
acquire behavior from their type that is not exposed to the normal inheritance search.

To lay the groundwork for understanding this distinction, the next section describes
the procedure Python follows to implement this instance-of type relationship.
'''

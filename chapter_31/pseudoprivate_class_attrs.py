"Pseudoprivate Class Attributes"
'''
Besides larger structuring goals, class designs often must address name usage too.
we noted that methods defined within a general
tool class might be modified by subclasses if exposed, and noted the tradeoffs of this
policy—while it supports method customization and direct calls, it’s also open to accidental
replacements.

classes—data hiding is a convention, and
clients may fetch or change attributes in any class or instance to which they have a
reference. In fact, attributes are all “public” and “virtual,” in C++ terms; they’re all
accessible everywhere and are looked up dynamically at runtime.
'''


"""
That said, Python today does support the notion of name “mangling” (i.e., expansion)
to localize some names in classes. Mangled names are sometimes misleadingly called
“private attributes,” but really this is just a way to localize a name to the class that
created it—name mangling does not prevent access by code outside the class. This
feature is mostly intended to avoid namespace collisions in instances, not to restrict
access to names in general; mangled names are therefore better called “pseudoprivate”
than “private.”

Pseudoprivate names are an advanced and entirely optional feature, and you probably
won’t find them very useful until you start writing general tools or larger class hierarchies
for use in multiprogrammer projects. In fact, they are not always used even when
they probably should be—more commonly, Python programmers code internal names
with a single underscore (e.g., _X), which is just an informal convention to let you know
that a name shouldn’t generally be changed (it means nothing to Python itself).
"""

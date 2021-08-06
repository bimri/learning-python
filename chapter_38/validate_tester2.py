"""
Unlike in the prior property-based variant, though, in this case the actual name value is
attached to the descriptor object, not the client class instance. Although we could store
this value in either instance or descriptor state, the latter avoids the need to mangle
names with underscores to avoid collisions. In the CardHolder client class, the attribute
called name is always a descriptor object, not data.
Importantly, the downside of this scheme is that state stored inside a descriptor itself
is class-level data that is effectively shared by all client class instances, and so cannot
vary between them. That is, storing state in the descriptor instance instead of the
owner (client) class instance means that the state will be the same in all owner class
instances. Descriptor state can vary only per attribute appearance.
"""

from __future__ import print_function                                   # 2.X
from validate_tester import loadclass

CardHolder = loadclass()
bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')

print('bob:', bob.name, bob.acct, bob.age, bob.addr)

sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
print('sue:', sue.name, sue.acct, sue.age, sue.addr)                    # addr differs: client data
print('bob:', bob.name, bob.acct, bob.age, bob.addr)                    # name,acct,age overwritten?


"""
The results confirm the suspicion—in terms of managed attributes, bob has morphed
into sue!

There are valid uses for descriptor state, of course—to manage descriptor implementation
and data that spans all instance—and this code was implemented to illustrate
the technique.
"""

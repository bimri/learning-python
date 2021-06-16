'''
Common application of lambda is to define inline 
callback functions forPython’s tkinter GUI API
'''
# creates a button that prints a message on the 
# console when pressed
import sys
from tkinter import Button, mainloop                                        # Tkinter in 2.X

x = Button(
    text='Press me',
    command=(lambda:sys.stdout.write)
)

x.pack()
mainloop()                                                                  # This may be optional in console mode

"defers execution of the handler until the event occurs lambda"


class MyGui:
    def makewidgets(self):
        Button(command=(lambda: self.onPress("spam")))                      # self had to be passed in to a lambda with defaults
    def onPress(self, message):
        ...use message...


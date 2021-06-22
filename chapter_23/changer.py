"reload Example"

message = 'After editing'
def printer():
    print('reloaded:', message)

"that actually returns the module object reload"
'''
if you use reload, you’ll probably want to pair it with
import instead of from, as the latter isn’t updated by reload operations

reload by itself updates only a single module, but it’s 
straightforward to code a function that applies it transitively to related modules
'''
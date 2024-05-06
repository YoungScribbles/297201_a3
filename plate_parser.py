
# -- token.py -- #

import re

NUMS = re.compile('[0-9]')


## CLASSES

# TODO Is a linked list the best data structure for this???
class TokList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        n = self.head
        while n.next:
            n = n.next
        n.next = Node(data)

    def debug(self):
        s = ''
        n = self.head

        while n:
            s += str(n.data)
            s += ','
            n = n.next
        print(s)

    def convert_to_uint8(self):
        n = self.head

        while n:
            c = convert_to_uint8(n.data)

            if c != None:
                n.data = c
            #else do nothing
            n = n.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## FUNCTIONS

def process_input(input):
    chars = list(input)
    ret = tokenise_input(chars)
    return ret

# Note: Recursive
def tokenise_input(input):
    tok = input.pop()

    if len(input) != 0:
        l = tokenise_input(input)
        l.append(tok)
    else:
        l = TokList(tok)

    return l
    

def convert_to_uint8(char):
    if type(char) != str:
        print('Error: %v is not of type str' % char)
        return None

    # if NUMS.match(char) != None:
    #     return char
    
    return ord(char)



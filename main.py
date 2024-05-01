
# 297201 - Assignment 3
#
#   M. Phillips
#   J. X
#   F. X
#
#   License plate model

## CLASSES

# TODO Is a linked list the best data structure for this???
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        n = self.head
        while n.next:
            n = n.next
        n.next = Node(data)

    def debug(self):
        n = self.head
        while n:
            print(n.data)
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
        l = LinkedList(tok)

    return l
    

# Tokenise input

a = 'Test Input a'
b = 'TeST inPUT b'
c = 'TEST INPUT C'

inputs = [a,b,c]

for s in inputs:
    print(s)
    l1 = process_input(s)
    l1.debug()

# from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    # Your code goes here.
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    # Your code goes here.
    node = None
    node = push(node, 3)
    node = push(node, 2)
    node = push(node, 1)
    return node

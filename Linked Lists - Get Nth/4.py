# from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):

    if node is None:
        raise Exception

    counter = 0
    current = node
    while current is not None:
        if counter == index:
            return current
        current = current.next
        counter += 1
    raise Exception

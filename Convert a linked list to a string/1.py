"""Convert a linked list to a string"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def stringify(node):
    result = []
    current = node
    while current is not None:
        result.append(str(current.data))
        current = current.next

    result.append('None')

    return ' -> '.join(result)

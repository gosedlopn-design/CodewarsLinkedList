"""Parse a linked list from a string"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:

    if list_repr == 'None':
        return None

    lst = list_repr.split(' -> ')
    lst.pop()
    node = None
    for el in lst[::-1]:
        node = Node(int(el), node)
    return node

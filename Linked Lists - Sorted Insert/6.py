class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):

    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node
    current = head
    prev = None
    while current is not None and current.data < data:
        prev = current
        current = current.next
    prev.next = new_node
    new_node.next = current
    return head

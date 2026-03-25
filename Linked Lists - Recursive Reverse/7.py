class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def reverse_recursion(current, prev):
        if current is None:
            return prev
        new_node = current.next
        current.next = prev
        return reverse_recursion(new_node, current)
    return reverse_recursion(head, None)

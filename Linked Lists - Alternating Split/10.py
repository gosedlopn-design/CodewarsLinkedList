class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise Exception
    current = head
    first = Node(None)
    second = Node(None)
    tail1 = first
    tail2 = second
    while current is not None and current.next is not None:
        tail1.next = current
        tail2.next = current.next
        
        tail1 = tail1.next
        tail2 = tail2.next
        
        current = current.next.next
    if current is not None:
        tail1.next = current
        tail1 = tail1.next
    tail1.next = None
    tail2.next = None
        
        
    return Context(first.next, second.next)

# from preloaded import Node
class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    
    node = Node(None)
    node.next = head
    prev = node
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next
        
        prev.next = second
        first.next = second.next
        second.next = first
        
        prev = first
        
    return node.next

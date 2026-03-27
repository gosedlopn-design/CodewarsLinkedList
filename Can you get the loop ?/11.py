class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
      
def loop_size(node):
    slow = node.next
    fast = node.next.next
    
    while slow != fast:
        fast = fast.next.next
        slow = slow.next
    current = slow.next
    count = 1
    while current != slow:
        current = current.next
        count += 1
    return count

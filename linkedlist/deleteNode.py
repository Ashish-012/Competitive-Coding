'''
    If the head is `None` return. Setup two pointers, one pointing to the previous node and one to the current node and one variable counting the
    positions. Traverse till we reach the end of the list or the position. After that check if we reach the position or not, if not then the position
    does not exists in the list. Check if the position is 0, if it is then just point head to the `current.next`. Otherwise point  prev.next to the
    current.next and set current to `None`. 
'''
def deleteNode(head, position):
    if not head:
        return head
    current = head
    prev = None
    pos = 0
    
    while current and pos != position:
        prev = current
        current = current.next
        pos += 1
    if pos!= position:
        return head
    elif pos == 0:
        head = current.next
        current = None
    else:
        prev.next = current.next
        current = None
    return head
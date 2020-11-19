'''
    Create the node with the data we want to insert. Check if the head is `None` means the list is empty, update the head with our node
    and return it. Create two nodes one pointing to the head and other to none and a pos variable to keep track of the position.
    Now iterate through the list updating the prev node to the current node and current to the next node, till we reach the position
    or we reach the end of the list. If the pos variable is not the same as the position that means we are at the end of the list and
    the position doesnot exist. Otherwise set the next of prev node to the node we created and its next to the current.
'''
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
        return head
    current = head
    prev = None
    pos = 0
    while current and pos!=position:
        prev = current
        current = current.next
        pos += 1
    
    if pos!= position:
        return head
    else:
        prev.next = node
        node.next = current
    return head
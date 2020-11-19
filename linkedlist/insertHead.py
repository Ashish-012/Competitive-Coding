'''
	Check if the list is empty, if it is just point the head to the new node created and return the head. Otherwise create a node `current` pointing
	to the head node. Now point the head node to the newly created node with the data and in the end point the next of the newly created node to 
	the `current`.
'''

def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
        return head
    
    current = head
    head = node
    node.next = current
    
    return head
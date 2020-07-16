"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev =  self.prev

        self.next = None
        self.prev = None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        new_node  = ListNode(value, None, None)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        if self.head :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # if DLL is empty
            # set head and tail to the new node instance
        else:
            self.head = new_node
            self.tail = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        old_head_value = self.head.value
        # decrement the length of the DLL
        self.length -= 1 
        # delete the head
            # if head.next is not None
                # set head.next's prev to None
                # set head to head.next
        if self.head.next is None:
            self.head.prev = None
            self.head = self.head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None
        else:
            self.head = None 
            self.tail = None

        # return the value
        return old_head_value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value, None, None)
        # increment the DLL length attribute
        self.length += 1 

        # if DLL is empty
            # set head and tail to the new node instance
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        old_tail_value = self.tail.value
        # decrement the length of the DLL
        self.length -= 1 
        # delete the tail
            # else (if tail.prev is None)
                # set head to None
                # set tail to None
        if self.tail.prev is None:
            self.head = None
            self.tail = None 

            # else tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
        else:
            self.tail.next = None
            self.tail = self.tail.prev
        # return the value
        return old_tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #Check if it's already in front and return
        if node is self.head:
            return
        #Delete the node we want to move 
        self.delete(node)
        #increase the length
        self.length += 1 
        node.next = self.head
        self.head.prev = node
        self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.length += 1
        node.prev = self.tail
        self.tail.next = node
        self.tail = node 

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #if list is empty
        if not self.head:
            print('ERROR : list is empty')
            return None
        
        self.length -= 1 

        #if list has one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        # if list has more than one item and the node to delete is the head node 
        if node == self.head:
            self.head = node.next
            self.tail = None 
        
        # if list has more than one item and the node to delete is the tail node
        if node == self.tail:
            self.tail = node.prev
            self.head = None 
        
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current.node = self.head
        highest_value = 0

        while current_node is not None:
            if highest_value < current_node.value:
                highest_value = current_node.value
            
            current_node = current_node.next
        
        return highest_value
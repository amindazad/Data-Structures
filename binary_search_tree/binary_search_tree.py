import sys
sys.path.append('../stack')
from stack import Stack
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
sys.path.append('../queue')
from queue import Queue

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    def __len__(self):
        return self.size
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    def dequeue(self):
        # handle if list is empty
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                 
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif (target < self.value) and (self.left is not None):
            return self.left.contains(target)
        elif (target > self.value) and (self.right is not None):
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else: 
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
            
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print()

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        queue = Queue()
        queue.enqueue(node)
        # Start by placing the root in the queue
        current_node = None
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
            # dequeue item from front of queue
            # print that item
        while (queue.size > 0):
            current_node = queue.dequeue()
            print(current_node.value)
            # place current item's left node in queue if not None
            if current_node.left:
                queue.enqueue(current_node.left)
            # place current item's right node in queue if not None
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize an empty stack
        # push the root node onto the stack

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
            # pop top item off the stack
            # print that item's value

            # if there is a right subtree
                # push right item onto the stack
                
            # if there is a left subtree
                # push left item onto the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

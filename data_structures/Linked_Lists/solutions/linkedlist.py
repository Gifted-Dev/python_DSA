"""
# Exercise: Linked List

1. In [LinkedList class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list.py) that we implemented in our tutorial add following two methods,
```
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
```
Now make following calls,
```
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
```
"""

#---------------CREATING CLASS NODE------------------#
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#-------------------CREATING LINKDEDLIST---------------#
class LinkedList:
    def __init__(self):
        self.head = None
    
    # ------------------------------------ #
        # METHOD TO PRINT LIST
    # ------------------------------------ #
    def print(self):
        if self.head is None:
            print("This list is empty")
            return 
        
        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.val) + "-->"  if itr.next else str(itr.val)
            itr = itr.next   
        print(llist)
    
    # ------------------------------------ #
        # METHOD TO INSERT VALUES
    # ------------------------------------ #
    def insert_values(self, values):
        if self.head is None:
            for value in values[::-1]:
                self.head = Node(value, self.head)
    
    
    # ------------------------------------ #
        # METHOD TO INSERT VALUE AFTER
    # ------------------------------------ #
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        itr = self.head

        # Now insert data_to_insert after data_after node
        while itr:
            if itr.val == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            itr = itr.next
    
    # ------------------------------------ #
        # METHOD TO REMOVE VALUE
    # ------------------------------------ #
    def remove_by_value(self, data):
        itr = self.head
        
        # Remove first node that contains data
        if itr and itr.val == data:
            self.head = self.head.next
            return
    
        while itr and itr.next:
            if itr.next.val == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        
        print(f"'{data} is not in the list")
 
### TEST PHASE ###

ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()

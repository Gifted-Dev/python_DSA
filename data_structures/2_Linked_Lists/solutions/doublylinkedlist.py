"""
2. Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction.
Your node class will look this this,
```
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
```
Add following new methods,
```
def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
```
Implement all other methods in [regular linked list class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list.py) and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

[Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/Solution/doubly_linked_list_exercise.py)
"""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # ------------------------------------ #
        # METHOD TO INSERT VALUES AT END
    # ------------------------------------ #
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
       
    
    # ------------------------------------ #
        # METHOD TO INSERT VALUES
    # ------------------------------------ #
    def insert_values(self, data):
        if self.head is None:
            for dat in data:
                self.insert_at_end(dat)
        else:
            for dat in data:
                    self.insert_at_end(dat)
        
  
    # ------------------------------------ #
        # METHOD TO PRINT VALUE FORWARD 
    # ------------------------------------ #
    
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("The list is empty")
            return
        
        itr = self.head
        llist = ''
        
        while itr:
            llist += str(itr.data) + '--->' if itr.next else str(itr.data)
            itr = itr.next
        print(llist)
            
    # ------------------------------------ #
        # METHOD TO PRINT VALUE BACKWARDS
    # ------------------------------------ #
    
    def print_backward(self):
    # This method prints list in backward direction
        if self.head is None:
            print("The list is empty")
            return
        
        last_node = self.get_last_item()
        itr = last_node
        llist = ''
        
        while itr:
            llist += str(itr.data) + '--->' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llist)
        
    # ------------------------------------ #
        # METHOD TO CHECK THE LAST VALUE
    # ------------------------------------ #
    def get_last_item(self):
    # This method print the last item
        if self.head is None:
            print("The list is empty")
            return
    
        itr = self.head
        
        while itr.next:
            itr = itr.next
        return itr        
    
    # ------------------------------------------- #
        # METHOD TO GET THE LENGTH OF THE LIST
    # ------------------------------------------- #
    def get_length(self):
        if self.head is None:
            print("The list is empty")
            return
        
        itr = self.head
        count = 0
        
        while itr:
            count += 1
            itr = itr.next
        return count
    
    
    
    
    # ------------------------------------ #
        # METHOD TO INSERT AT INDEX
    # ------------------------------------ #
    def insert_at(self, index, data):
        new_node = Node(data)
        length = self.get_length()
        if self.head is None:
            print(f"Empty List, {data} placed at index 0")
            self.head = new_node
            return
        
        if index < 0:
            index += length
            return
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            return
            
        if index > length:
            print("Index Out of range, input a valid index")
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                new_node.next = itr.next
                itr.next = new_node
            itr = itr.next
            count += 1
        return itr
        
        



            
ll = DoublyLinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print_forward()
ll.print_backward()
ll.insert_at_end("figs")
ll.print_forward()
ll.insert_at(0,"jackfruit")
ll.print_forward()
ll.insert_at(6,"dates")
ll.print_forward()
ll.insert_at(2,"kiwi")
ll.print_forward()
    
    
    
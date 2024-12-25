# An example trying to understand how linkedlist works

"""
    In a linked list, we have the following: 1. Node 2. head or tails indicator
    What does a Node have: A data and a pointer
    
    What methods should a link list have:
    - Print the items in the list
    - Add an item to the beginning of the list
    - Add an item to the end of the list
    - Remove an item from an index of the list
    - Insert at any index of the list
    - insert another list to the end of the list
    """

# creating a node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
# creating a linkedlist
class Linkedlist:
    def __init__(self):
        self.head = None
        
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------    
        
    # create a method to print the items in the list
    def print_list(self):
        """
        Steps take to print the items in a linked list:
        - Confirm if list is empty i.e. head is none:
            if yes: return list is empty, 
            if not: Proceed
        - Set head to iter, loop through the list, and print each list.
        """
        if self.head is None:
            print("This list is empty")
            return 
        
        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + "-->"  if itr.next else str(itr.data)
            itr = itr.next   
        print(llist)
        
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    
    # create a method to add an item to the beginning of the list
    def insert_to_beginning(self, data):
        
        """
        Steps to insert at the beginning of the list
        - the function takes in a value, and creates a node with the data
        - The node points to the head of the list
        - And the node is assigned to become the head       
        """
        
        if self.head is None:
            self.head = Node(data)
            return
        
        node = Node(data, self.head)
        self.head = node
        
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    
    # create a method to insert item to end of list
    def insert_to_end(self, data):
        """
        Steps taken to insert to the end of the list
        - check if the list is empty, then set list as head
        - if list is empty, set new node as head
        - if list is not empty, iter to the last item
        - the point to the node
        """
        if self.head is None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
           itr = itr.next
           
        itr.next = Node(data)
    
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    
    # create a method to get the length of the list
    def get_length(self):
        """
        Steps to get the length of the list
        0. Check if list is empty
        1. create a count to zero
        2. iter through the list and increase the count
        """
        
        if self.head is None:
            print("The list is empty")
            return
        
        count = 0
        itr = self.head
        
        while itr:
            itr = itr.next
            count += 1
        
        return count
    
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    
    # create a method to remove an item from an index of the list
    def remove_at(self, index):
        """
        steps taken to remove at a particiular index
        1. check if index is within list range, if not raise an Exception error
        2. set count to zero
        3. loop through the list
        4. if count is before the index, skip the next node        
        """
        length = self.get_length() # gets the length of the list
        
        if index < 0: # solves minus index, -1 == max(length)
            index += length
        
        if index >= length: # if index is greater than list, raise error
            raise Exception("Input a valid index")
        
        if index == 0: # if index is set to 0, shift th ehead to the next node
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next
           
           
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
        
            
    # Insert at any index of the list
    def insert_at(self, index, data):        
        if self.head is None: # check if 
            self.head = Node(data)
            return
        
        if index == 0:
            # self.head = Node(data, self.head): this works too... 
            self.insert_to_beginning(data)
            return
        
        count = 0
        itr = self.head
        
        while itr.next:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                return
            count += 1
            itr = itr.next

    
        
    # Insert another list to the end of the list
    def insert_list_end(self, datalist):
        if self.head is None:
            self.head = self.insert_to_end(datalist)
            return
        
        itr = self.head
        
        while itr.next:
            if itr.next is None:
                self.head = self.insert_to_end(datalist)
            itr = itr.next
            
    def insert_list_beginning(self, datalist):
        if self.head is None:
            print("list is empty")
        
        for data in datalist[::-1]:
            self.insert_to_beginning(data)
    
    
    
    
    
    
    
        

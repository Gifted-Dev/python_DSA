from linkedlist_classes import *


mylist = Linkedlist()

# printing the empty list
mylist.print_list()

# Adding items to the beginning of the list
mylist.insert_to_beginning(5)
mylist.insert_to_beginning(10)
mylist.insert_to_beginning(20)

# insert to the end of the list and print
mylist.insert_to_end(7)
mylist.print_list()

# remove at index two of the list and print
mylist.remove_at(1)
mylist.print_list()

# insert at a particular index
mylist.insert_at(0, 29)
mylist.print_list()

# insert list to end
mylist.insert_list_beginning([3,4,5])
mylist.print_list()
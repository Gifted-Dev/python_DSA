class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    # add child
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
                return
            self.left = BinarySearchTree(data)
        
        if data > self.data:
            if self.right:
                self.right.add_child(data)
                return
            self.right = BinarySearchTree(data)
            
    # search
    def search(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                self.left.search(data)
                
        if data > self.right:
            if self.right:
                self.right.search(data)
                
        return False
                
    
    # inorder traversal
    def inorder_traversal(self):
        element = []
        
        if self.left:
            element += self.left.inorder_traversal()
    
        element.append(self.data)
        
        
        if self.right:
            element += self.right.inorder_traversal()
            
        return element
        
        
    
    # preorder traversal
    def preorder_traversal(self):
        elements = [self.data]
        
        # if self.data:
        #     elements.append(self.data)
            
        if self.left:
            elements += self.left.preorder_traversal()
            
        if self.right:    
            elements += self.right.preorder_traversal()
        
        return elements
        
        
    # post order traversal
    def postorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.postorder_traversal()
        
        if self.right:
            elements += self.right.postorder_traversal()
        
        elements.append(self.data)
        
        return elements
    
    def find_min(self):
        # Making use of inorder_traversal
    #    item = self.inorder_traversal()
    #    num = item[0]
    #    return num
        if self.left:
           return self.left.find_min()   
        return self.data


    def find_max(self):
        # This also works, Use of iteration
        # current = self
        # while current.right:
        #     current = current.right
        # return current.data
        
        # Applying recursion
        if self.right:
            return self.right.find_max()
        return self.data
    
    def delete(self, val):
        if val < self.data: # if value is less than the root data
            if self.left:  # Then it will be in the left node, if the left node exists
                self.left = self.left.delete(val) # then recursively check through the left node 
        elif val > self.data: # if the value is now greater than the root data
            if self.right: #then the value is at the right node, check if right node exist
                self.right = self.right.delete(val) # then recursively check through the right node for the value
        else: # When the value equates the data, i.e. when val == self.data
            if self.left is None and self.right is None: # if there are no leaves node
                return None # delete the node i.e. self.data
            if self.left is None: # if there is only one child at the right child and none at the left
                return self.right # return the right child 
            if self.right is None: # if there is only one child at the left node and none at the right
                return self.left # return the left child
            
            max = self.left.find_max() # find the largest value at the left sub tree
            self.data = max # equate it to the root data
            self.left = self.left.delete(max) # delete the copy of the max node
        return self


    def sum_elements(self):
        # Although this works
        # item = self.inorder_traversal()
        # total = sum(item)
        # return total
        
        # perfect way to do it
        if self is None:
            return 0
        
        return self.data + (self.left.sum_elements() if self.left else 0) + \
                           (self.right.sum_elements() if self.right else 0)
    
        
    
def CreateBinaryTree(element):
    root = BinarySearchTree(element[0])
    
    for i in range(1, len(element)):
        root.add_child(element[i])
        
    return root
            
    
if __name__ == '__main__':
    root_tree = CreateBinaryTree([15, 12, 34, 12, 32, 5,6, 11,13,15,16])
   
    print(root_tree.inorder_traversal())
    
    print(root_tree.preorder_traversal())
    print(root_tree.postorder_traversal())
    print(root_tree.find_min())
    print(root_tree.find_max())
    print(root_tree.sum_elements())
    root_tree.delete(16git)
    print(root_tree.inorder_traversal())

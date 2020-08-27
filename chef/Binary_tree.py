
"""
binary trees have at most two child nodes.
binary serch trees are a special case of binary trees and they have
an order where the nodes on the left are smaller than the father and
the nodes on the right are grater than the father, olso elements are 
unique. (serching hear is very easy).
en python se puede ocupar mayor e igual simbolos con strings basado en
orden alfabetico.
  
"""

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
            
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
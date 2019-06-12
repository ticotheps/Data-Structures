#--------------BINARY SEARCH ALGORITHM---------------
    #  ***Assumes that the input array is alrady sorted
    #  Find midpoint
    #  Check the midpoint element of the input array against target
    
    #  PSEUDOCODE
        #  if target == input[midpoint], then return the midpoint index
            #  do this again, with just the LEFT subarray
        #  OTHERWISE, if target > input[midpoint]
            #  do this again, with just the RIGHT subarray
            
#--------------BINARY SEARCH TREE DATA STRUCTURE---------------
    #   Kind of like a data structure that is used for sorting data
    #   BST is REALLY good for search because it is VERY FAST
        #  ***TRADE-OFF: Slower insertion
    #   First element in the array = the root element
    
    #   STEPS FOR CREATING BINARY SEARCH TREE DATA STRUCTURE:
        #  1) Compare the element against the current node's value.
        #  2) Based on the result of the comparison, go LEFT or RIGHT
        
    #   Example 1: 
        #  Insert: 15, 11, 13, 13
    #
    #                     (15)
    #                     /       <== arrows go to the LEFT b/c 11 < 15
    #                  (11)
    #                    \        <== arrows go to the RIGHT b/c 13 > 11
    #                    (13)
    #                      \      <== arrows go to the RIGHT b/c 13 = 13
    #                      (13)
    
    #   Example 2: 
    #
    #                     (21)
    #                    /    \         
    #                (18)      (25)
    #               /    \     /   \  
    #            (14)   (19) (23)  (28)
    #               \          \       
    #               (15)       (24)
    
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        #  ***Don't forget to wrap the value in a node!***
        #  1) Compare the element against the current node's value
        #  2) Based on the result of the the comparison, go LEFT or RIGHT
        #  3) If we find an empty spot, park the value there
        #  4) Otherwise, go back to Step 1
        
        #  What is the base case?
        #  Base Case: We've found an empty spot where we can add the value
        if value < self.value:
            #  If value is less, we go LEFT
            #  If there is no left child, we can park this node here
            if not self.left:
                self.left = BinarySearchTree(value)
            #  Recurse on the left child
            else: 
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        pass
      
    def get_max(self):
        pass
      
    def for_each(self, cb):
        pass
      
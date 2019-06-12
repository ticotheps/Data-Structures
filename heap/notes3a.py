#---------------------HEAPS------------------------
    #  Objective: optimal access to priority elements
        #  i.e. - max, min, longest string, etc.
    #  Used for: sorting, logging
    #  Application: We want to be able to access the priority element in
    #               O(1) run time.
    
    #  How can I access something in O(1) time?
        #  Array indexing
            #  (assuming we know the index of what we want to access)
        #  By key (in a hash table)
        #  By reference (the root of the tree)
        
    #  INSERT & DELETE: The heap still needs to maintain the priority
        #  Insertion: What happens when we insert a new priority element?
        #  Deletion: What happens when we delete the priority element?
            #  How do we determine the NEXT priority element?
    
    #  EXAMPLE 1: TREE REPRESENTATION OF THE HEAP
    #
    #                     (100)
    #                    /    \         
    #                (19)      (36)
    #               /    \     /   \  
    #            (17)    (3) (25)  (1)
    #            /  \                 
    #          (2)  (15)     
    
    #  - Notice that the heap does not follow the same rules as the BST.
    #  - The only thing that a heap cares about is that the children element are   #    LESS priority than the parent element.
    
    #  Getting MAX heap => O(1)
        #  return self.root.value
        
    #  DELETION: 
    #    => Removes the hightest priority element
    #    => Find the NEXT highest priority element to fill in the newly vacated position
    
    #  "SIFTING DOWN" STEPS:
    #    => Save a reference to the old priority element so we can return it
    #    => Overwrite the old priority element with the last element in the array
    #    => Remove the last element from the array, because we don't want multiple
    #       copies
    #    => Sift down the element at index 0.
    
    #  INSERTION: 
    #    => Removes the hightest priority element
    #    => Find the NEXT highest priority element to fill in the newly vacated 
    #       position
    
        #  Check Parent vs Children (during insertion)
        #    => left child: 2 * index + 1
        #    => right child: 2 * index + 2
        #    => parent: (index - 1) / 2
        
    #  "BUBBLING UP" STEPS:
    #    => Append new element to the end of the array
    #    => Bubbled the new element up the heap until it reaches a valid spot
    #    => Remove the last element from the array, because we don't want multiple
    #       copies
    #    => Bubble up the element at index 0.
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
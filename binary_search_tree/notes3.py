#--------------BINARY SEARCH TREES---------------
    #  ***Assumes that the input array is alrady sorted
    #  Find midpoint
    #  Check the midpoint element of the input array against target
    
    #  PSEUDOCODE
        #  if target == input[midpoint], then return the midpoint index
            #  do this again, with just the LEFT subarray
        #  OTHERWISE, if target > input[midpoint]
            #  do this again, with just the RIGHT subarray
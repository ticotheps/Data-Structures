class Heap:
    def __init__(self, comparator=0):
        self.storage = []
        self.last_index = -1
        self.comparator = comparator
        self.length = len(self.storage)

    def insert(self, value):
        self.last_index += 1
        if self.last_index < len(self.storage):
            self.storage[self.last_index] = value
        else:
            self.storage.append(value)
        self._bubble_up(self.last_index)

    def delete(self):
        if self.last_index == -1:
            return "Unable to delete from an empty heap"
        
        min_value = self.storage[0]
        
        self.storage[0] = self.storage[self.last_index]
        self.last_index -= 1
        self._sift_down(0)
        
        return min_value

    def get_max(self, index):
        if index == 0:
            return None, None
          
        self.comparator = (index - 1) / 2
        
        return self.comparator, self.storage[self.comparator]
      	# if self.length >= 1:
        #     min_value = self.storage[1]         
        #     self.length -= 1
        #     self.storage[1], self.storage[self.last_index] = self.storage[self.last_index], self.storage[1]  #swap root with last_index element
        #     self.last_index -= 1               #decrement length
        #     self.storage.pop(-1)          #pop the root that was moved to the last_index element
        #     if self.length>1:          #coz first item is None
        #         if self.length<=2:
        #             self.storage[1:]=sorted(self.storage[1:]) #use reverse=True for max-heap
        #         else:
        #             self._sift_down(index)
        #     return min_value

    def get_size(self):
        return self.last_index + 1

    def _bubble_up(self, index):
        while self.comparator > 0:
            self.comparator, self.storage[self.comparator] = self.get_max(index)
            
            if self.storage[self.comparator] <= self.storage[index]:
                break
              
            self.storage[self.comparator], self.storage[index] = self.storage[index], self.storage[self.comparator]
            
            index = self.comparator

    def _sift_down(self, index):
        while True:
            index_value = self.storage[index]       
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            
            if left_child_index > self.last_index:
                return None, index_value
            elif left_child_index < self.last_index:
                return left_child_index, self.storage[left_child_index]
              
            if right_child_index > self.last_index:
                return None, index_value
            elif right_child_index < self.last_index:
                return right_child_index, self.storage[right_child_index]
            
            self.storage[index_value], self.storage[index] = self.storage[index], self.storage[index_value]
            
            index = index_value

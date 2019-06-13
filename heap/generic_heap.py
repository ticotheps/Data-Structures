class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        self.last_index = -1
        self.comparator = comparator

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

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass

class BinarySearchTree:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return str(target)+" not found"
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else: 
            return True

    def get_max(self):
      pass

    def for_each(self, cb):
      pass
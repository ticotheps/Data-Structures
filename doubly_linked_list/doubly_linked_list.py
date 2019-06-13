"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
          current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
          current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
          self.prev.next = self.next
        if self.next:
          self.next.prev = self.prev
          
    #  Returns next ListNode
    def get_next(self):
        return self.next

    #  Sets next ListNode to 'node' argument
    def set_next(self, next):
        self.next = next
        
    #  Returns next ListNode
    def get_prev(self):
        return self.prev

    #  Sets next ListNode to 'node' argument
    def set_prev(self, prev):
        self.prev = prev
 
    #  Sets next ListNode to 'node' argument
    def get_value(self, prev):
        return self.value      
        

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, value, node=None):
        self.value = value
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            return
        new_node = ListNode(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self
    
    def printList(self):
        array = []
        currentNode = self.head
        while currentNode is not None:
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)

    def remove_from_head(self):
        pass
        #  Checks for empty list
        #  Sets head to "temp"
        #  Sets current head to head.next
        #  Deletes temp
        #  If head is not NONE, head.prev = None
        # if not self.head:
        #     return False
        # else:
        #     temp = self.head
        #     self.head = self.head.next
        #     del temp
        #     if self.head is not None:
        #         self.head.prev = None
        # return temp

    def add_to_tail(self, value):
        if self.head is None:  #  <== if a head doesn't exist...
            new_node = ListNode(value)  #  <== creates a new instance of a ListNode!
            self.head = new_node  #  <== sets the new_node as the NEW current tail
            return
        currentNode = self.head
        while currentNode.next is not None:  #  <== if the current node's next-pointer is pointing to 'None', which is 'False'...
            currentNode = currentNode.next  #  <== reaches the 2nd to last node of the list and sets the that node's tail's next-pointer to point to the the last node.
        new_node = ListNode(value)  #  <== creates a new instance of a ListNode! 
        currentNode.next = new_node  #  <== sets the tails's current 'next-pointer' to reference the new_node
        new_node.prev = currentNode  #  <== sets the new_node's 'prev-pointer' to reference the old tail
        self.length += 1  #  <== increases the length of the doubly linked list by 1
        
    def remove_from_tail(self):
        if self.tail is None:
            return "This list has no item to delete"
        if self.tail.next is None:
            self.tail = None
            return
        while self.tail.next is not None:
            self.tail.next.prev.next = None

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        # pass
        if self.head is None:
            print("There is no element to delete.")
            return
        if self.head.next is None:
            if self.head.value == node:
                self.head = None
            else:
                print("Node not found")
            return
        if self.head.value == node:
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is not None:
            if n.value == node:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.pref = n.prev
        else:
            if n.value == node:
                n.prev.next = None
            else:
                print("Node not found")
      
    def get_max(self, arr):
        valuesArr = []
        for i in range(len(arr)):
            if self.tail.next is not None:
                valuesArr.append(arr[i])
        return max(valuesArr)
    
myDLL = DoublyLinkedList(2)
myDLL.add_to_head(4)
myDLL.add_to_head(7)
myDLL.add_to_tail(5)
myDLL.printList()
myDLL.delete(7)
myDLL.printList()

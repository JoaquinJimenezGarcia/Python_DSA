class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head, self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        return True
    
    def pop(self):
        if self.length == 0:
            return False
        
        if self.length == 1:
            self.head = None
            self.tail = None
        
        temp = self.head

        while temp is not None:
            temp = temp.next
            
            if temp.next.next is None:
                self.tail = temp
                self.tail.next = None
                
                temp = None
                self.length -= 1


    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head, self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

            return True
        
        if self.length == 0:
            return False
        
        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp
    
    def get(self, index):
      if self.length == 0 or index < 0 or index >= self.length:
          return None
      
      if self.length == 1:
          return self.head
      
      temp = self.head
      
      for _ in range(index):
        temp = temp.next
        
      return temp
    
    def set_value(self, index, value):
      if self.length == 0 or index < 0 or index >= self.length:
          return None
        
      temp = self.head
      
      for _ in range(index):
        temp = temp.next
      
      temp.value = value
    
    def insert(self, index, value):
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_linked_list = LinkedList(4)
my_linked_list.print_list()

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(9)
print("First entire LL:")
my_linked_list.print_list()

my_linked_list.pop()
print("LL poped")
my_linked_list.print_list()

my_linked_list.append(12)
my_linked_list.append(14)
print("LL with new last value", my_linked_list.length)
my_linked_list.print_list()

print("LL with prepend")
my_linked_list.prepend(100)
my_linked_list.print_list()

print("LL with first pop")
my_linked_list.pop_first()
my_linked_list.print_list()
print("Get index of X", my_linked_list.get(2).value)

print("LL with the index 0 modified")
my_linked_list.set_value(0, 99)
my_linked_list.set_value(3, 0)
my_linked_list.print_list()
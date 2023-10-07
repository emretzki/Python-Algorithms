class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
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
            

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
        return True

    def pop(self, value):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None            
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        
        new_node = Node(value)
                
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return True
    
    def popFirst(self):
        
        if self.length == 0:
            return None
        
        elif self.length == 1:
            temp = self.head.value
            
            self.head = None
            self.tail = None
            print(str(temp) + " is popped")
            
        else:
            pre = self.head.next
            self.head = None    
            self.head = pre
        self.length -= 1
        return True
            
        
        
            
        


my_linked_list = LinkedList(5)
# my_linked_list.append(2)
# my_linked_list.append(11)
# my_linked_list.append(9)
# my_linked_list.prepend(3)
my_linked_list.popFirst()

# print('Head next:', my_linked_list.head.next.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
my_linked_list.print_list()


                                                                                                                    
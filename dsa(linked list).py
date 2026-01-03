print("-"*(50))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        
    def add_at_position(self, position, data):
        new_node = Node(data)
        temp = self.head
        pos = 0
        while pos < position-2 and temp.next:
            temp = temp.next
            pos+=1
        new_node.next = temp.next
        temp.next = new_node
    
    def add_at_value(self,value, data):
        new_node = Node(data)
        if self.head is None:   ## exception when there is only one data except none it raises as none type has nno data
            self.head = new_node
        elif self.head.next.data > value and self.head.next:
                new_node.next = self.head
                self.head = new_node

        else:
            temp = self.head
            while temp.next:
                if temp.data == value:
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                    return
                elif temp.next.data > value:
                    new_node.next = temp.next
                    temp.next = new_node
                else:
                    temp = temp.next
                    if temp.next is None:
                        new_node.next = temp.next
                        temp.next = new_node
                        break
            

        
    
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head = self.head.next
        
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is None")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
        
    def delete_at_position(self, position):
        temp = self.head
        pos = 0
        while temp.next.next and pos < position-2:
            temp = temp.next
            pos +=1
        temp.next = temp.next.next

    def delete_the_value(self, key):
        if self.head is None:
            print("Linked list in empty")
        else:
            temp = self.head
            pos = 0
            while temp.next:
                if temp.next.data == key:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                pos +=1
            else:
                print(f"{key} not found")
                

    def display(self):
        if self.head is Node:
            print("Linked list is none")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="-> ")
                temp = temp.next
            print("None")


## creating objects
ll1 = LinkedList()
ll1.display()
ll1.add_at_beginning(24)
ll1.display()
ll1.add_at_end(27)
ll1.display()
ll1.add_at_position(2,26)
ll1.display()
ll1.add_at_position(2,25)
ll1.display()
ll1.add_at_position(5,30)
ll1.display()
ll1.add_at_beginning(20)
ll1.display()
ll1.delete_at_beginning()
ll1.display()
ll1.delete_at_end()
ll1.display()
ll1.delete_at_position(3)
ll1.display()
ll1.delete_the_value(27)
ll1.display()
ll1.add_at_value(28, 32)   ## worked
ll1.display()
ll1.add_at_value(12, 13)
ll1.display()
ll1.add_at_value(25,26)
ll1.display()
ll1.add_at_value(24, 24.5)
ll1.display()


## veery good all well.abs# except for exception of add at value where only one data is in linked list . check out that :)
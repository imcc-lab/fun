class Node:
    data = 0
    next = None
    
class LinkedList:
    head = None
    def create(self,data):
        if self.head == None:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            self.head = new_node
        else:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if self.head == None:
            print("LinkedList is empty")
        else:
            temp = self.head
            while temp!=None:
                print(temp.data,end="->")
                temp = temp.next

    def count(self):
        c = 0
        temp = self.head
        while temp!=None:
            c+=1
            temp = temp.next
        return c

    def insert(self,data,pos):
        size = self.count()
        print(size)
        if size<pos:
            print("Position not in range of Linkedlist")
        else:
            c = 1
            temp = self.head
            while pos!=c:           #for i in range(1,pos): 
                c+=1                   # temp = temp.next
                temp = temp.next
            new_node = Node()
            new_node.data = data
            new_node.next = temp.next
            temp.next = new_node

    def delete(self,data):
        temp = self.head
        while temp.data!=data:
            temp = temp.next
            print(temp.data)
        
        
            


x = LinkedList()
x.display()
x.create(44)
x.create(55)
x.create(88)
x.create(83)
x.create(89)
x.display()
print()
print("Total Nodes are : ",x.count())
x.insert(9999,2)
x.display()
x.insert(888,4)
x.display()
print()
x.delete(55)
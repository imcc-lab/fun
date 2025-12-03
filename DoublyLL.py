class Node:
    data = 0
    prev,link = None,None

class DoublyLinkedList:
    head = None

    def append(self,data):
        if self.head == None:
            self.head = Node()
            self.head.data = data
            self.head.prev = None
            self.head.link = None
        else:
            new_node = Node()
            new_node.data = data
            new_node.link = None
            temp = self.head
            while temp.link != None:
                temp = temp.link
            new_node.prev = temp
            temp.link = new_node

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" -> ")
            temp = temp.link
        print()

    def insert_at_beginning(self,data):
        if self.head == None:
            self.head = Node()
            self.head.data = data
            self.head.prev = None
            self.head.link = None
        else:
            new_node = Node()
            new_node.data = data
            new_node.prev = None
            new_node.link = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_by_pos(self,pos):
        c = 0
        temp = self.head
        while temp != None:
            c+=1
            temp = temp.link
        if pos>c or pos<0:
            print("Position is out of range")
        else:
            temp2 = self.head
            for i in range(1,pos):
                temp2 = temp2.link
            temp3 = temp2.prev
            temp4 = temp2.link
            temp3.link = temp4
            temp4.prev = temp3

    def search_element(self,data):
        temp = self.head
        c = 0
        while temp != None:
            c += 1
            if temp.data == data:
                print("Found at Position : ",c)
                break
            temp = temp.link
        else:
            print("Not Found")

    def count(self):
        c = 0
        temp = self.head
        while temp != None:
            temp = temp.link
            c+=1
        return c

    def delete_middle(self):
        c = self.count()
        mid = c//2
        self.delete_by_pos(mid)

    def reverse_list(self):
        temp = self.head
        while temp.link != None:
            temp = temp.link
        while temp != None:
            print(temp.data,end = "->")
            temp = temp.prev
        print()


x = DoublyLinkedList()
x.insert_at_beginning(83)
x.print_list()
x.append(44)
x.append(89)
x.append(12)
x.append(90)
x.print_list()
x.insert_at_beginning(54)
x.print_list()
x.delete_by_pos(3)
x.print_list()
x.search_element(89)
x.count()
x.delete_middle()
x.print_list()
x.reverse_list()
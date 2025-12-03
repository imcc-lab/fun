class Node:
    data = 0
    link = None

class SinglyLinkedList:
    head = None

    def append(self,data):
        if self.head == None:
            self.head = Node()
            self.head.data = data
            self.head.link = None

        else:
            new_node = Node()
            new_node.data = data
            new_node.link = None
            temp = self.head
            while temp.link != None:
                temp = temp.link
            temp.link = new_node

    def print_list(self):
        if self.head == None:
            print("Linked List is empty..")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" -> ")
                temp = temp.link
            print()

    def insert(self,pos,data):
        c = 0
        temp = self.head
        while temp!=None:
            c+=1
            temp = temp.link
        if pos>c or pos<0:
            print("Position out of range")
        else:
            new_node = Node()
            new_node.data = data
            temp = self.head
            for i in range(1,pos):
                temp = temp.link
            new_node.link = temp.link
            temp.link = new_node

    def delete_last(self):
        temp = self.head
        while temp.link != None:
            temp2 = temp
            temp = temp.link
        temp2.link = None
        print(temp.data,"-> removed..")

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

    def print_max(self):
        list_data = []
        temp = self.head
        while temp != None:
            list_data.append(temp.data)
            temp = temp.link
        print("Maximum from list : ",max(list_data))

    def print_min(self):
        list_data = []
        temp = self.head
        while temp != None:
            list.data.append(temp.data)
            temp = temp.link
        print("Minimum from list : ",min(list_data))

    def count_even_odd(self):
        even,odd = 0,0
        temp = self.head
        while temp != None:
            if temp.data%2==0:
                even+=1
            else:
                odd+=1
            temp = temp.link
        print("Even : ",even)
        print("Odd : ",odd)

    def merge_list(self,list1):
        temp = self.head
        while temp.link != None:
            temp = temp.link
        temp.link = list1.head
        list1.head = self.head
        self.print_list()

    def reverse_list(self):
        temp = self.head
        list_data = []
        while temp != None:
            list_data.append(temp.data)
            temp = temp.link
        list_data.reverse()
        print(list_data)

    def next_greater(self):
        list1 = []
        temp = self.head.link
        temp2 = self.head
        while temp!=None:
            if temp.data > temp2.data:
                list1.append(temp.data)
            else:
                list1.append(0)
            temp2 = temp
            temp = temp.link
        list1.append(0)
        print(list1)



z = SinglyLinkedList()
z.append(3)
z.append(5)
z.append(8)
z.append(2)
z.next_greater()

x = SinglyLinkedList()
x.print_list()
x.append(44)
x.append(88)
x.append(77)
x.append(22)
x.append(85)
x.append(3)
x.print_list()
print("----------------------")
x.next_greater()
x.insert(2,99)
x.print_list()
x.delete_last()
x.print_list()
x.search_element(88)
x.search_element(988)
x.search_element(44)

x.print_max()
x.count_even_odd()

y = SinglyLinkedList()
y.append(83)
y.append(32)
y.append(96)
y.append(28)
y.append(10)
y.print_list()


x.merge_list(y)
x.reverse_list()




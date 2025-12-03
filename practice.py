class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class singly:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            temp = self.head
            while temp.link != None:
                temp = temp.link
            temp.link = new_node

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" -> ")
            temp = temp.link
        print()



x = singly()
x.append(44)
x.append(22)
x.print_list()
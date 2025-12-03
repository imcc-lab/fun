class Node:
    data = 0
    link = None

class dyStack:
    top = None
    def push(self,data):
        new_node = Node()
        new_node.data = data
        new_node.link = self.top
        self.top = new_node

    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            c = self.top.data
            self.top = self.top.link
            return c

    def display(self):
        temp = self.top
        print("Top")
        while temp!=None:
            print(temp.data)
            temp = temp.link

x = dyStack()
x.push(33)
x.push(88)
x.push(99)
x.display()
x.pop()
print()
x.display()
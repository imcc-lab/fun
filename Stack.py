class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return 0
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def reverse(self):
        rev = []
        for i in range(len(self.stack)-1,-1,-1):
            rev.append(self.stack[i])
        return rev

    def display(self):
        print("Stack:", self.stack)


# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.display()
# print("Reverse : ",s.reverse())
#
# print("Top element:", s.peek())
# print("Popped : ",s.pop())
# s.display()
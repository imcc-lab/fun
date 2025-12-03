class linearStack:
    top = -1
    Max = 10
    data = []
    def __init__(self):
        for i in range(0,self.Max):
            self.data.append(0)

    def push(self,no):
        self.top+=1
        self.data.append(no)




x = linearStack()
x.push(33)

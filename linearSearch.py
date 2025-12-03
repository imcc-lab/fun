def linearSearch(a,no):
    
    for i in a:
        if i == no :
            index = a.index(no)
            print("Found at : ",index)
            break
    else :
        print("Not Found")

a = []
number = int(input("Enter number of elements : "))
for i in range(number):
    no = int(input("Enter Number : "))
    a.append(no)

b = int(input("Enter number to be searched : "))
linearSearch(a,b)
def binary_search(a,n,no):
    f = 0
    l = n-1
    while f<=l:
        m = int((f+l)/2)
        if no == a[m]:
            index = a.index(no)
            print("Found at index : ",index)
            break
        elif no > a[m]:
            f = m+1
        else:
            l = m-1
    else:
        print(no,' Not Found')

a = []
n = int(input("Enter n : "))
for i in range(n):
    d = int(input('Enter Number : '))
    a.append(d)

a.sort()
print(a)
no = int(input("Enter to number to be searched : "))
binary_search(a,n,no)
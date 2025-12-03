def binary_search(array,size,number):
    f = 0
    l = size-1
    while f<=l:
        m = int((f+l)/2)
        if number == array[m]:
            index = array.index(number)
            print("Found at index : ",index)
            break
        elif number > array[m]:
            f = m+1
        else:
            l = m-1
    else:
        print(number,' Not Found')

array = []
size = int(input("Enter n : "))
for i in range(size):
    d = int(input('Enter Number : '))
    array.append(d)

array.sort()
print(array)
number = int(input("Enter to number to be searched : "))
binary_search(array,size,number)
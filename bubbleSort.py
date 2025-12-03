def bubble_sort(x):
    for i in range(0,n-1,1):
        for j in range(0,n-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]

x = []
n = int(input("Enter n : "))
for i in range(n):
    no = int(input("Enter number : "))
    x.append(no)

print("Before sorting : ")
print(x)
bubble_sort(x)
print("After sorting : ")
print(x)
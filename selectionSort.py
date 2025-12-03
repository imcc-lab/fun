def selection_sort(x):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if x[i]>x[j]:
                x[i],x[j] = x[j],x[i]
                
x = []
n = int(input("Enter n : "))
for i in range(n):
    no = int(input("Enter number : "))
    x.append(no)



print("Before Sort : ")
print(x)
selection_sort(x)
print("After sort : ")
print(x)
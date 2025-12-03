def insertion_sort(a):
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if a[i]>a[j]:
                t = a[i]
                a[i] = a[j]
                for k in range(j,i,-1):
                    a[k] = a[k-1]
                a[i+1]=t

x = []
n = int(input("Enter n : "))
for i in range(n):
    no = int(input("Enter number : "))
    x.append(no)

print("BEFORE SORT : ")
print(x)
insertion_sort(x)
print("AFTER SORT : ")
print(x)
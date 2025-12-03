def quicksort(a,f,l):
     if f < l:
          p = a[f]
          i = f+1
          j = l
          while i<=j:
               
               while i<=l and p>=a[i]:
                    i = i+1
                    
               while p<a[j]:
                    j=j-1

               if i<j:
                    a[i],a[j] = a[j],a[i]

          a[f] = a[j]
          a[j] = p
          quicksort(a,f,j-1)
          quicksort(a,j+1,l)

x = []
n = int(input("enter n : "))

for i in range(n):
     no = int(input("enter no : "))
     x.append(no)

print("Display Elements Before Quick Sort")
print(x)

quicksort(x,0,n-1)

print("Display Elements After Quick Sort")
print(x)

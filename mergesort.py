def mergesortt(a,f,l):
       if f<l:
            
            m = int((f+l)/2)
            
            mergesortt(a,f,m)
            
            mergesortt(a,m+1,l)
            merge(a,f,m,l)
            
def merge(a,f,m,l):
     
     b = []
     i = f
     j = m+1
     while i<=m and j<=l:
          if a[i] < a[j]:
               b.append(a[i])
               i=i+1
          else:
               b.append(a[j])
               j=j+1
               
     while i<=m:
          b.append(a[i])
          i=i+1
          
     while j<=l:
          b.append(a[j])
          j=j+1

     i = f
     for no in b:
          a[i] = no
          i=i+1

x = []
n = int(input("enter n : "))

for i in range(n):
     no = int(input("enter no : "))
     x.append(no)

print("Display Elements Before Merge Sort")
print(x)


mergesortt(x,0,n-1)

print("Display Elements After Merge Sort")
print(x)

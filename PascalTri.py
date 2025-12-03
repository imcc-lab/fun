n = 7
spaces = 7
for i in range(1,n+1):
    for j in range(0,spaces):
        print(" ",end=" ")
    c = 1
    for j in range(1,i+1):
        print(c,end="   ")
        c = c*(i-j)//j
    spaces-=1
    print()
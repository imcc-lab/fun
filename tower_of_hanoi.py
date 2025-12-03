def toh(n,A,B,C):
    if n==1:
        print("Move disk from source",A," destination",C)
        return
    toh(n-1,A,C,B)
    toh(1,A,B,C)
    toh(n-1,B,A,C)

n=3
toh(n,'A','B','C')
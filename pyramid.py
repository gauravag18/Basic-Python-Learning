
n=int(input("number of rows"))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()

for i in range(n+1,1,-1):
    for j in range(n+1-i,1,-1):
        print(" ",end="")
    for k in range(2*i,1,-1):
        print("*",end="")
    print()
     
r=int(input("Enter any integer "))
c=int(input("Enter any integer "))
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()

r=4
c=4
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j!=c-1:
            print("_",end="")
    print()
    
r=5
c=4
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
        if j!=c-1:
            print(" ",end="")
    print()

c=int(input("Enter the value of c "))
for i in range(c):
    for j in range(c-i):
        print("*",end="")
    print()

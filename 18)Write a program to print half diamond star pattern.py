n=int(input())
m=int(input())
for i in range(n):
    for i in range(i+1):
        print("*",end="")
    print()
for i in range(m):
    for i in range(i-1,2):
        print("*",end="")
    print()

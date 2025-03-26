
print()
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
for i in range(0,r):
    for j in range(0,i+1):
        print("*",end="")
    print()    

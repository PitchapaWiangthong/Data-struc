n = int(input("Enter Input : "))
n1,n2,n3,n4=n+2,n+2,n+2,n+2

for row_top in range(1,n1+1):
    for point_top in range(1,n1):
        print(".",end='')
    for colum_top in range(row_top):
        print("#",end='')
    if row_top == 1 or row_top == n2:
        print("+"*n2,end='')
    else:
        print("+"+"#"*(n2-2)+"+",end='')
        
    print(end="\n")
    n1-=1

for row_down in range(1,n3+1):

    if row_down == 1 or row_down == n4:
        print("#"*n4,end='')
    else:
        print("#"+"+"*(n4-2)+"#",end='')

    for point_down in range(1,n3+1):
        print("+",end='')
    for colum_down in range(row_down-1):
        print(".",end='')
    print(end="\n")
    n3-=1
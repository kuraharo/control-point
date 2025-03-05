a=int(input())
b=int(input())
c=int(input())
d=int(input())
print()
mat=[[0 for i in range(d-c+2)] for j in range(b-a+2)]
for i in range(1,b+2-a):
    for j in range(1,d+2-c):
        mat[i][j]=(a+i-1)*(c+j-1)
mat[0][0]="*"
cons=1
for i in range(a,b+1):
    mat[cons][0]=i
    cons+=1
cons=1
for j in range(c,d+1):
    mat[0][cons]=j
    cons+=1

for i in range(0,b+2-a):
    for j in range(0,d-c+2):
        print(mat[i][j],end=" ")
    print()
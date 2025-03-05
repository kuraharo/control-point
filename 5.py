str1=str(input())
str2=str(input())
if len(str1)!=len(str2):
    print("error разные длины строк")

flag=5
for i in range(1,len(str1)-1):
    for j in range(i+1,len(str1)):
        if(str1[0:i]+str1[j]+str1[i+1:j]+str1[i]+str1[j+1:len(str1)]==str2):
            print("true")
            flag=1


if flag==5:
    print("false")

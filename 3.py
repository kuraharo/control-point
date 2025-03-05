string1=str(input())
string2=''
flag=0
constanta=1
flag=0
for i in range(len(string1)-1):
    if(string1[i]==string1[i+1]):
        constanta+=1
    else:
        string2=string2+string1[flag]+str(constanta)
        constanta=1
        flag=i+1

if(string1[-1]==string1[-2]):
    string2=string2+string1[flag]+str(constanta)
else:
    string2=string2+string1[flag]+str(constanta)+string1[-1]+"1"
    constanta=1
    flag=i+1

print(string2)
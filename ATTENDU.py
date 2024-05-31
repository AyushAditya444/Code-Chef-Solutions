# cook your dish here
from collections import Counter
for i in range(int(input())):
    int1=int(input())
    str1=input()
    dict1=Counter(str1)
    int2=120-int1
    int3=((int2+dict1["1"])/120)*100
    if int3>=75:
        print("YES")
    else:
        print("NO")
    
    
# cook your dish here
from collections import Counter
for _ in range(int(input())):
    int1=int(input())
    str1=input()
    str2=input()
    dict1=Counter(str1)
    dict2=Counter(str2)
    if dict1==dict2:
        print("YES")
    else:
        print("NO")
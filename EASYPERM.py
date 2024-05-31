# cook your dish here
for _ in range(int(input())):
    int1=int(input())
    list1=[]
    for i in range(int1):
        list1.insert(0,i+1)
    print(*list1)
    
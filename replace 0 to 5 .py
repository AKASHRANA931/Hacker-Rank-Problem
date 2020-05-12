# 1st logic here
a = map(int,input().split())
a1 = []
for i in a:
    if(i == 0):
        i = 5
        a1.append(i)
    else:
        a1.append(i)
result = ""
for i in a1:
    result = result + str(i)
print(int(result))
    
    
#2nd logic here

list = []
n = int(input())
m = len(str(n))
while(n>0):
    digit = n % 10
    if(digit == 0):
        digit = 5
        list.append(digit)
        n = n // 10
    else:
        list.append(digit)
        n = n // 10
    stack = list[::-1]
    result = ""
    for i in stack:
        result = result + str(i)
    print(int(result))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys,itertools
if sys.version_info[0]>=3:
    ainput=int(input())
a=input().split()
k=int(input())
num=0
den=0
for e in itertools.permutations(a,k):
    den+=1
    num+='a' in e[:k]
print(num*1.0/den)

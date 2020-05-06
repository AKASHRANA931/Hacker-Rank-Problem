import re
N = int(input())
for i in range(N):
    a = str(input())
    l = len(a)
    matchObj = re.search("^[789][0-9]{9}$", a)
    if matchObj:
        print "YES"
    else:
        print "NO"

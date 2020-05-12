list = []
def case(s):
    global list
    for i in s:
        
        if(i.isupper()):
            a = i.lower()
            list.append(a)
        elif(i.islower()):
            b = i.upper()
            list.append(b)
        else:
            list.append(i)

s = str(input(""))
case(s)
for i in list:
    result = ""
    result = result + str(i)
    print(result,end="")

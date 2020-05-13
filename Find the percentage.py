#Akash Rana
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #for fetching the score of this name input by user(query_name)
    scoreList = student_marks[query_name]
    #for find the total sum of score(one by one)
    scoresum = 0
    for i in scoreList:
        scoresum = scoresum + i
    #for average percentage
    averagescore = (scoresum)/3
    print("%.2f" % averagescore)
    
   #2nd method


n = int(input())
file = {}
for i in range(n):
    name = str(input())
    file[name] = {int(input()) for i in range(n)}
print(file)
name1 = str(input())
a = file[name1]
sum = 0
for i in a:
    sum = sum + i
ave = sum/2
print("%.2f"% ave)

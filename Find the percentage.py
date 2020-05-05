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

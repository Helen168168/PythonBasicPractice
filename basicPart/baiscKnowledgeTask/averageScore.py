#统计考试成绩的平均分
def average_score(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum / len(scores)
scores = [90, 80, 85, 70, 60]
average = average_score(scores)
print(average)




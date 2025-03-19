'''
挑战1分钟内可以答对几道数学运算题目
直接在控制台使用命令行运行
程序运行之后倒计时1分钟之后结束
随机出100以内的2个整数加减乘除运算题目（除法确保能够除尽，但除数不能为0）
每出一道题目，由玩家给出答案，然后程序判断对错，接着出下一题，并且显示剩余时间
1分钟时间结束，显示总题数和正确率（正确率精确到小数点后2位），并将之前的题目和答案显示出来

考察的知识点
格式化字符串输出、循环、条件判断、列表、异常处理、自定义函数、时间工具包、随机工具包、包导入

思考过程：
1.获取两个随机整数
2.随机一个加减乘除的运算符
2.判断运算符后计算结果
3.判断用户输入的结果是否正确
4.计算总题数和正确率
5.计时
6.时间结束后展示显示题目和答案
'''

import random
import time

def calcMathTask():
    correctCount = 0
    totalCount = 0
    questionList = []
    answerList = []
    startTimer = time.time()
    print(startTimer)
    while time.time() - startTimer < 60:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        else:
            if operation == '/' and num1 % num2 != 0:
                result = num1 / num2

        question = f'{ num1 } { operation } { num2 } = ?'
        print(question)
        answer = input('请输入答案：')
        try:
            answer = int(answer)
        except ValueError:
            continue
        if answer == result:
            correctCount += 1
        totalCount += 1
        questionList.append(question)
        answerList.append(answer)
    print(f'总题数：{ totalCount }，正确率：{ correctCount / totalCount: .2f }')
    for i in range(len(questionList)):
        print(f'{ questionList[i] } { answerList[i] }')

calcMathTask()
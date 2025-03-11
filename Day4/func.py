'''
1.打印两个数相加
2.打印传入的参数
'''
def calcSum(num1, num2):
    result = num1 + num2
    print(f'num={num1}, num2={num2}, result={result}')
    return result
calcSum(1, 45) #位置参数
calcSum(num2 = 1, num1 = 45) #关键字参数

#可选参数 *类似解构
def optionalParams(*params):
    print(params) #(1,2,3,4,5)
    print(type(params)) #<class ‘tuple>
optionalParams(1,2,3,4,5)
tupleVal = (1, 2, 3, 4, 5)
optionalParams(tupleVal) #((1, 2, 3, 4, 5))
optionalParams(*tupleVal) #(1, 2, 3, 4, 5)

#可选关键字参数
def optionalKeyParams(**params):
    print(params) #{'name': 'Tom', 'age': 18}
    print(type(params))
optionalKeyParams(name = 'Tom', age = 18)

dicVal = { 'name': 'Tom', 'age': 18 }
optionalKeyParams(**dicVal)

#形参包含位置参数、可选参数和关键字参数
def allParams(param1, *param2, param3 = 2):
    print(f'param1={param1}')
    print(f'param2={param2}')
    print(f'param3={param3}')

allParams(1, 2, 3, 4, 5, param3 = 3) #param1=1
allParams(1, (2, 3, 4, 5), 'param3') #因此可选参数放在所有形参的最后位置最佳

#函数返回多个值
def returnMultiValue(param1, param2, param3, param4):
    return param1, param2, param3, param4
val1, val2, val3, val4 = returnMultiValue(1, 2, 3, 4)




# 这就是行注释
'''这就是多行注释'''
"""这就是多行注释"""

# 查看Python内置的关键字
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


# 数据类型

# int类型
intNum = 999
# 类似JavaScript的模版字符串
print(f'copyIntNum = { intNum }')
print(f'copyIntNum = { intNum }, type(intNumType) = { type(intNum) }')


# float类型
floatNum = 34.56
print(f' type(floatNumType) = {type(floatNum)}')

# bool 布尔类型 只有两个值True或者False
isShowVal = True | False
print(f' type(isShowValType) = {type(isShowVal)}')

# 字符串类型 三种定义方法,前两种用于单行数据定义，后两种用于多行数据定义
# 第一种: 'HelloWrold'
# 第二种: "HelloWrold"
# 第三种: '''HelloWrold'''
# 第四种: """HelloWrold"""
stringValue = """HelloWrold"""
print(f' type(stringValueType) = {type(stringValue)}')

#字符串截取
str = 'Hello World!'
print(f'str[2] = {str[2]}')
print(f'str[-1] = {str[-1]}')
print(f'str[0:3] = {str[0:3]}')
print(f'str[-1:0] = {str[-1:0]}')
print(f'str[-1:] = {str[-1:]}')
print(f'str[7:22] = {str[10:22]}')

# List列表类型，键有序、可重复、可拓展
listValue = ['HelloWorld', "I", "am", "a", 'Chinese', 'am', 'Chinese']
print(f'copyTupleValue = {listValue}, type(listValueType) = {type(listValue)}')

# tuple元组类型 键有序、可重复、不可拓展
tupleValue = ('HelloWorld', "I", "am", "a", 'Chinese', 'am', 'Chinese')
print(
    f'copyTupleValue = {tupleValue}, type(tupleValueType) = {type(tupleValue)}')

# Set 集合类型 无序、不可重复、不可拓展, 无序通过一套算法实现，使用当前时间戳变量定义键，因此元素的存储顺序与插入顺序无关
collectionValue = {'HelloWorld', "I", "am", "a", 'Chinese', 'am', 'Chinese'}
print(
    f'copyTupleValue = {collectionValue}, type(collectionValueType) = {type(collectionValue)}')


# Dictionary 字典类型， 键值对格式
dicValue = {'id': '1001', 'name': '雪梅', 'career': 'freelancer'}
print(f'copyDicValue = {dicValue}, type(dicValueType) = {type(dicValue)}')

# .format 填充参数 
num1 = 10
num2 = 20
num3 = 30
print('num1 = {0}, num2 = {1}, num3 = {2}'.format(num1, num2, num3));
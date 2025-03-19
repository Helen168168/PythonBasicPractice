from  enum import Enum

class FRUITE(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3

'''
访问枚举
'''
#访问枚举成员名称
print(FRUITE.APPLE.name)
#访问枚举成员值
print(FRUITE.APPLE.value)
#获取枚举类型
print(FRUITE.APPLE)

'''
枚举比较
使用is和==进行比较，is比较的是内存地址，==比较的是值，不可使用大小比较
'''
isEqual = FRUITE.APPLE is FRUITE.APPLE
print(isEqual)

'''
遍历枚举
'''
#遍历枚举类型
for type in FRUITE:
    print(f'menuType = {type}')

#遍历枚举名
for members in FRUITE.__members__:
    print(f'members = {members}')

#遍历枚举名和枚举类型
for name, type in FRUITE.__members__.items():
    print(f'name = {name}, type = {type}')


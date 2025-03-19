'''
类变量和实例变量的访问、区别及执行顺序
变量检索机制：先检查对象的__dict__字典中是否存在这个属性；如果不存在，则继续在类的__dict__中寻找。这种顺序确保了对象可以覆盖其所属类的属性值。
'''

#不使用self初始化变量
class Fruit:
    price = 5
    color = 'green'
    taste = 'sweet'

    def __init__(self, color, price):
        color = color
        price = price
#实例化对象
apple = Fruit('red', 6)
#打印类属性
print(f'apple_properties: { Fruit.price }')
#打印实例属性
print(f'class_properties: { apple.price }')

#使用self初始化变量
class Fruit:
    price = 5
    color = 'green'
    taste = 'sweet'
    def __init__(self, color, price):
        self.color = color
        self.price = price
        self.__class__.price = 12 + price #修改类属性,通过__class__访问类属性
    def discount(self):
        return self.price * 0.8

apple = Fruit('red', 6)
orange = Fruit('orange', 5)

#打印类属性
print(f'apple_properties: { Fruit.price }')
#打印实例属性
print(f'class_properties: { apple.price }')
#通过实例访问类属性
print(f'class_properties: { apple.__class__.price }')



# 打印类的所有属性
print(f'class_properties: { Fruit.__dict__ }')
#打印实例的所有属性
print(f'apple_properties: { apple.__dict__ }')
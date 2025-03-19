'''
类方法和实例方法的区别、定义和调用
'''

class Fruit:
    price = 5
    color = 'green'
    taste = 'sweet'

    def __init__(self, color, price):
        self.color = color
        self.price = price
    def discount(self):
        return self.price * 0.8
    @classmethod
    def classInfo(cls):
        cls.price += 1 # 修改类属性的值
        return cls.price

apple = Fruit('red', 6)
orange = Fruit('orange', 5)

# 调用类方法
print(Fruit.classInfo()) # 6
print(apple.classInfo()) # 7 不推荐这样调用，根据单一原则类方法应该由类调用并修改类属性

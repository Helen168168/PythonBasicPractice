'''
静态方法
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

    @staticmethod
    def staticInfo():
        print(f'class_variable: {Fruit.price}')

        return 'this is a static method'

apple = Fruit('red', 6)

# 调用静态方法
print(Fruit.staticInfo()) # this is a static method
print(apple.staticInfo()) # this is a static method

# 工具类-MathUtils类，其中包含一些与数学相关的工具函数
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# 使用静态方法
result1 = MathUtils.add(5, 3)  # 输出: 8
result2 = MathUtils.multiply(4, 2)  # 输出: 8
print(result1, result2)
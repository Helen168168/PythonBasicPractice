'''
私有属性和方法
在变量或方法名前加上双下划线(__)表示该成员为私有，Python会对其进行名称改写（例如 _ClassName__variableName），可以通过查看对象的__dict__属性得到验证。
动态添加私有变量：尝动态地给对象添加带有双下划线前缀的新属性时，这些属性不会作为真正的私有变量处理，而是成为普通的、可公开访问的属性。
Python并不会完全阻止外部访问私有变量，只是增加了访问难度。如__score可以通过ClassName__score形式被访问到，但基于封装原则，不推荐这样做。
'''

class Fruit:
    price = 5
    color = 'green'
    taste = 'sweet'
    __smell = 'good' # 私有属性
    def __init__(self, color, price):
        self.color = color
        self.price = price
    def discount(self):
        return self.price * 0.8
    @classmethod
    def classInfo(cls):
        cls.price += 1 # 修改类属性的值
        return cls.price
    def __privateMethod(self):
        print('this is a private method')

apple = Fruit('red', 6)

print(f'查看类所有属性和成员：{Fruit.__dict__}')
#访问私有属性
print(apple.__smell) # good

#动态添加私有变量
apple.__fresh = 'fresh'
orange = Fruit('orange', 5)
print(f'访问动态创建的私有属性：{orange.__fresh}') #报错。因为动态添加的私有属性并不是真正的私有属性，而是此对象的普通的属性


'''
类的定义和使用
'''

#错误示例
# class FruitError:
#     color = 'green'
#     price = 5
#     def discount():
#         return price * 0.8

#正确示例
class Fruit:
    color = 'green'
    price = 5
    def __init__(self, color, price):
        self.color = color
        self.price = price
    def discount(self):
        return self.price * 0.8

apple = Fruit('red', 6)
orange = Fruit('orange', 5)
strain = Fruit('yellow', 4)

# 查看对象的内存地址
appleId = id(apple)
orangeId = id(orange)
strainId = id(strain)
print(f'appleId = {appleId}, orangeId = {orangeId}, strainId = {strainId}')

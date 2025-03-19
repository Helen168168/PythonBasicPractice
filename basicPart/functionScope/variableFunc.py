'''
变量作用域
1.全局作用域
2.局部作用域
'''

varibaleVal = 23 # 全局变量

def setBlockVariable(x, y):
    varibaleVal = x + y # 局部变量
    print(f'func_varibaleVal = {varibaleVal}') # 30

setBlockVariable(10, 20)
print(f'global_varibaleVal = {varibaleVal}') # 23

def setGlobalVariable():
     price = 30
# print(f'varibaleVal = {price}') # 报错找不到全局变量price

#Python里面没有块级作用域
def judgeExecutionFunc():
    unitPrice = 20
    count = 2
    for i in range(1, 5):
        totalPrice = unitPrice * count
        print(f'total_price = {totalPrice}')
        totalCount = count + 1
    print(f'total_count = {totalCount}')



'''
永辉超市 TShirt 的单价是 56.5，裤子的单价是 89.8。风姐买了 3 件 TShirt，5 条裤子。
请写程序计算风姐一共该给多少钱？如果是老板生日，全场打 88 折，风姐又需要付多少钱呢？
'''
# 方法一 程序自定义数值
tShirtPrice = 56.5
tShirtCount = 3
pantPrice =  89.8
pantCount =  5
discount = 0.88
totalPrice = tShirtPrice * tShirtCount + pantCount * pantPrice
discountTotalPrice = totalPrice * discount
print('总价：%.2f, 折扣价：%.2f' % (totalPrice, discountTotalPrice))

# 方法2 使用input函数自行输入数值
tShirtPrice = input('请输入TShirt 的单价：')
tShirtCount = input('请输入TShirt 的数量：')
pantPrice = input('请输入裤子的单价：')
pantCount =  input('请输入裤子的数量：')
discount = input('请输入折扣：')
totalPrice = float(tShirtPrice) * int(tShirtCount) + float(pantCount) * int(pantPrice)
discountTotalPrice = totalPrice * float(discount)
print('总价：%.2f, 折扣价：%.2f' % (totalPrice, discountTotalPrice))



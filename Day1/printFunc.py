'''
练习：
1. 定义字符串变量 name，输出 我的名字叫 xxx，正在学习Python！
2. 定义字符串变量 name，整数变量 age，输出 我的名字叫 xxx，今年 x 岁，正在学习Python！
3. 定义小数 price、weight、money，输出 苹果单价 4.00 元/斤，购买了 3.00 斤，需要支付 12.00 元
'''

# 定义字符串变量 name，输出 我的名字叫 xxx，正在学习Python！
name = '彭雪梅'
print(f'我的名字叫 {name}，正在学习Python！')


#定义字符串变量 name，整数变量 age，输出 我的名字叫 xxx，今年 x 岁，正在学习Python！
name1 = 'pengxuemei'
age = 12
print(f'我的名字叫{ name1 }，今年{ age }岁，正在学习Python！')

# 定义小数 price、weight、money，输出 苹果单价 4.00 元/斤，购买了 3.00 斤，需要支付 12.00 元
price = 4.00
weight = 3.00
money = price * weight
print('苹果单价 %.2f 元/斤，购买了 %.2f 斤，需要支付 %.2f 元' % (price, weight, money));

# 定义一个小数scale，输出 数据比例是 10.00%
scale = 12.00
print('数据比例是 %.2f%%' % (scale, ))
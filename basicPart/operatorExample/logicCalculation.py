# 练习逻辑运算、if分支
month = input('please input month: ')
month = int(month)
if month <= 4 and month >= 2:
  print('month belong to the Spring')
elif month <= 7 and month >= 5:
  print('month belong to the Summer')
elif month <= 10 and month >= 8:
  print('month belong to the Autumn')
elif month == 12 or month == 11 or month == 1:
  print('month belong to the Winter')

'''
计算三个值的最大值
方法1: 使用if...elif...else判断
方法2: 三目运算符判断
'''

num1 = 12
num2 = 24
num3 = 2
# 方法一 

if num1 > num2:
  if num1 > num3:
    print(f'方法一 num1 = { num1 }是最大的')
  else:
    print(f'方法一 num3 = { num3 }是最大的')
else:
  if num2 > num3:
    print(f'方法一 num2 = { num2 }是最大的')
  else:
    print(f'方法一 num3 = { num3 }是最大的')

# 方法二

secondMax = num1 if num1 > num2 else num2
maxVal = secondMax if secondMax > num3 else num3
print(f'方法一 maxVal = {maxVal}是最大值')
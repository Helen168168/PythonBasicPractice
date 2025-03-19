'''
实现一个石头剪刀布
1 代表石头，2代表剪刀，3代表布
'''

import random

finger1 = random.randint(1, 3)
finger2 = int(input('请输入你的猜拳：'))
 
if finger1 == 1 and finger2 == 3 or finger1 == 2 and finger2 ==  1 or finger1 == 3 and finger2 == 2:
  print("你猜对了")
elif finger1 == finger2:
  print("平局")
else:
  print("很遗憾你猜错了！")

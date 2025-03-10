'''
找出1-100之间的偶数
使用循环方法while, for...in..., range
'''
num = 1
# while循环
while num <= 100:
 if num % 2 == 0:
  print(num)
 num = num + 1


# for...in...循环

for item in range(1, 101):
 if num % 2 == 0:
  print(num)



# range 循环
for item in range(2, 101, 2):
  print(item)


  '''
  使用for...else实现：用户输入密码，有三次机会，如果正确则登录成功否则冻结账户
  '''



for count in range(1, 4):
  password = input("please input password: ")
  if(password == '123456'):
   print('you are right')
else:
 print('you forget your password!')
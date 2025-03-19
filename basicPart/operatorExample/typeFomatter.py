# 整数转换 (int())
x = int(3.14)  # 浮点数转整数，结果为 3
y = int("123")  # 字符串转整数，结果为 123
z = int(True)  # 布尔值转整数，True 为 1，False 为 0

#  浮点数转换 (float())
x = float(3)  # 整数转浮点数，结果为 3.0
y = float("3.14")  # 字符串转浮点数，结果为 3.14
z = float(True)  # 布尔值转浮点数，True 为 1.0，False 为 0.0

# 字符串转换 (str())
x = str(123)  # 整数转字符串，结果为 "123"
y = str(3.14)  # 浮点数转字符串，结果为 "3.14"
z = str(True)  # 布尔值转字符串，结果为 "True"

# 布尔值转换 (bool())
x = bool(0)  # 整数 0 转布尔值，结果为 False
y = bool(1)  # 非零整数转布尔值，结果为 True
z = bool("")  # 空字符串转布尔值，结果为 False
w = bool("Hello")  # 非空字符串转布尔值，结果为 True

#  列表转换 (list())
x = list((1, 2, 3))  # 元组转列表，结果为 [1, 2, 3]
y = list("Hello")  # 字符串转列表，结果为 ['H', 'e', 'l', 'l', 'o']
z = list({1, 2, 3})  # 集合转列表，结果为 [1, 2, 3]

# 元组转换 (tuple())
x = tuple([1, 2, 3])  # 列表转元组，结果为 (1, 2, 3)
y = tuple("Hello")  # 字符串转元组，结果为 ('H', 'e', 'l', 'l', 'o')
z = tuple({1, 2, 3})  # 集合转元组，结果为 (1, 2, 3)

#  集合转换 (set())
x = set([1, 2, 2, 3])  # 列表转集合，结果为 {1, 2, 3}（去重）
y = set("Hello")  # 字符串转集合，结果为 {'H', 'e', 'l', 'o'}
z = set((1, 2, 3))  # 元组转集合，结果为 {1, 2, 3}

#  字典转换 (dict())
x = dict([(1, 'one'), (2, 'two')])  # 列表转字典，结果为 {1: 'one', 2: 'two'}
y = dict(a=1, b=2)  # 关键字参数转字典，结果为 {'a': 1, 'b': 2}

#  字节转换 (bytes())
x = bytes("Hello", encoding="utf-8")  # 字符串转字节，结果为 b'Hello'
y = bytes([1, 2, 3])  # 列表转字节，结果为 b'\x01\x02\x03'

#  字节数组转换 (bytearray())
x = bytearray("Hello", encoding="utf-8")  # 字符串转字节数组
y = bytearray([1, 2, 3])  # 列表转字节数组

#  复数转换 (complex())
x = complex(3, 4)  # 创建复数 3 + 4j
y = complex("3+4j")  # 字符串转复数，结果为 3 + 4j
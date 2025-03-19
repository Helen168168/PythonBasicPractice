'''
#杨辉三角
数字排列成三角形，每一行的数字是上一行相邻两个数字之和
'''

def yanghui_triangle(n):
    items = []
    for i in range(n):
        items.append([1] * (i + 1))
        for j in range(1, i):
            items[i][j] = items[i - 1][j - 1] + items[i - 1][j]
    for item in items:
        for num in item:
            print(num, end=' ')
        print()
yanghui_triangle(10)
# 列表找最大元素
def find_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
lists = [12, 3, 556, 23, 45, 67, 89, 100]
maxVal = find_max(lists)
print(maxVal)
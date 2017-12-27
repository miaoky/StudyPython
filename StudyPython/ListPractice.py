practiceList1 = [1, 2, 3]
practiceList2 = [4, 5, 6]
practiceSet = set([7, 8, 9])
print(practiceList1 + practiceList2)
print(len(practiceList1))
print(practiceList1 * 2)
print(3 in practiceList1)
print(practiceList1[:2])
print(practiceList1[-1:])

# 返回列表元素最大值
print(max(practiceList1))

# 返回列表元素最小值
print(min(practiceList1))

# 将元组转换为列表
print(practiceSet)
print(list(practiceSet))

# 在列表末尾添加新的对象
practiceList1.append(0)
print(practiceList1)

# 统计某个元素在列表中出现的次数
print(practiceList1.count(0))

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
practiceList1.extend(practiceList2)
print(practiceList1)

# 从列表中找出某个值第一个匹配项的索引位置
print(practiceList1.index(1))

# 将对象插入列表
practiceList1.insert(2, 11)
print(practiceList1)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(practiceList1)
practiceList1.pop()
print(practiceList1)
practiceList1.pop(2)
print(practiceList1)

# 移除列表中某个值的第一个匹配项
print(practiceList1)
practiceList1.remove(practiceList1[0])
print(practiceList1)

# 反向列表中元素
practiceList1.reverse()
print(practiceList1)

# 列表排序
practiceList1.sort()
print(practiceList1)

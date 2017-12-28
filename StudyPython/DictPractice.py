testDict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# 计算字典元素个数，即键的总数
print(len(testDict))

# 输出字典，以可打印的字符串表示
print(str(testDict))

# 返回输入的变量类型，如果变量是字典就返回字典类型
print(type(testDict))

# 返回一个字典的复制
copyDict = testDict.copy()
print(copyDict)

# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
newDict = testDict.fromkeys(["Name", "Class", "Age", 7], 4)
print(newDict)

# 删除字典内所有元素
testDict.clear()
print(testDict)
print(copyDict)

# 返回指定键的值，如果值不在字典中返回default值
print(copyDict.get("Name", "1"))
print(copyDict.get("Name1", "1"))

# 如果键在字典dict里返回true，否则返回false
print("Name" in copyDict)

# 以列表返回可遍历的(键, 值) 元组数组
print(copyDict.items())

# 以列表返回一个字典所有的键
print(copyDict.keys())

# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(copyDict.setdefault("Name", "1"))
print(copyDict.setdefault("Name1", "1"))

# 把字典dict2的键/值对更新到dict里
copyDict.update({"Sex": "男"})
print(copyDict)

# 以列表返回字典中的所有值
print(copyDict.values())

# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值,default默认为None
print(copyDict.pop("Name1", "1"))
print(copyDict)

# 随机返回并删除字典中的一对键和值(一般删除末尾对)。
print(copyDict.popitem())
print(copyDict)

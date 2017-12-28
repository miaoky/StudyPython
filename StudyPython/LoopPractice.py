for i in range(5):
    print(i)
else:
    print("end")

# 使用range指定区间的值
for i in range(5, 10):
    print(i)

# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
for i in range(10, 15, 2):
    print(i)

while i < 96:
    i += 2
else:
    print("i>96")

# pass 不做任何事情，一般用做占位语句
for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
    if i == 2:
        pass
    print(i)

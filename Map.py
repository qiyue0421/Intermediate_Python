"""1、map函数"""
# Map会将一个函数映射到一个输入列表的所有元素上
# 规范：map(function_to_apply, list_of_inpits)

# 大多数情况下，我们要把列表中所有元素一个个地传递给一个函数，并收集输出
items1 = [1, 2, 3, 4, 5]
squared = []
for i in items1:
    squared.append(i**2)
print(squared)

# map可以提供一种漂亮的方式实现相同的功能
items2 = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items2))  # 多数情况下，我们使用匿名函数lambda来配合map
print(squared)


# 可以用于一列表的函数
def multiply(x):
    return x * x

def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    print(list(map(lambda x: x(i), funcs)))


"""2、filter函数"""

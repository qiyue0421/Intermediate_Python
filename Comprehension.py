# 推导式（解析式）是python的一种独有特性，是可以从一个数据序列构建另一个新的数据序列的结构体，共有三种推导：

# 列表推导式：提供了一种简明扼要的方法来创建列表
# 它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是0个或多个for或者if语句，返回结果将是一个新的列表
# 规范：
# variable = [out_exp for out_exp in input_list if out_exp == 2]
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
print([x**2 for x in range(10)])


# 字典推导式
some_dict = {'a': 3, 'b': 4, 'A': 5, 'c': 2 }
print({k: v for k, v in some_dict.items()})
print({v: k for k, v in some_dict.items()})  # 快速对换一个字典的键和值


# 集合推导式
# 和列表推导式类似，唯一的区别在于它们使用大括号
print({x**2 for x in range(10)})

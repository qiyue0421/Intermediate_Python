# 自省（introspection），在计算机计算领域里是指在运行时来判断一个对象的类型的能力。Python中一切皆对象

# dir是用于自省的最重要函数之一，返回一个列表，列出了一个对象所拥有的属性和方法
my_list = [1, 2, 3]
print(dir(my_list))


# type函数返回一个对象的类型
print(type(''))
print(type([]))
print(type({}))
print(type(dict))
print(type(3))


# id函数返回任意不同种类对象的唯一ID
name = 'qiyue'
print(id(name))


# inspect模块也提供了很多有用的函数，来获取活跃对象的信息
import inspect
print(inspect.getmembers(str))

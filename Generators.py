# 可迭代对象（Iterable）：python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了一个可以支持下标索引的__getitem__方法，那么它就是一个可迭代对象。
# 简单地说，可迭代对象就是能提供迭代器的任意对象

# 迭代器（Iterator）：任意对象，只要定义了next（python2）或者__next__方法，它就是一个迭代器

# 迭代（Iteration）：简单地说，就是从某个地方（比如一个列表）取出一个元素的过程，当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代

# 生成器（Generators）：也是一种迭代器，但是只能对其迭代一次，这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。通过遍历来使用它们，要么用一个"for"循环，
# 要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数的形式来实现的，然而，它们并不返回一个值，而是yield一个值


def generator_function():
    for i in range(3):
        yield i


for item in generator_function():
    print(item, end=' ')


# 生成器的最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中（消耗大量资源），特别是结果集中还包含循环，许多Python2里的标准库函数都会返回列表，
# 在python3修改成了返回生成器，因为生成器占用更少的资源
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for x in fibon(50):
    print(x, end=' ')
print()


# python内置函数：next() 用于获取一个序列的下一个元素
gen = generator_function()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# print(next(gen))  # yield完所有值后，触发一个StopIteration异常，提示所有的值都被取完了，注意：for循环会自动捕获该异常并停止调用next()


# str对象是否支持迭代？
my_string = 'qiyue'
# next(my_string)
"""
# 异常说明str对象不是一个迭代器
Traceback (most recent call last):
  File "D:/Pycharm/Intermediate_Python/Generators.py", line 45, in <module>
    next(my_string)
TypeError: 'str' object is not an iterator
"""
# str对象是一个可迭代对象，而不是一个迭代器，这意味着它支持迭代，但我们不能直接对其进行迭代操作。可以使用内置函数iter()，它可以根据一个可迭代对象返回一个迭代器对象
my_iter = iter(my_string)
print(next(my_iter))  # q
print(next(my_iter))  # i

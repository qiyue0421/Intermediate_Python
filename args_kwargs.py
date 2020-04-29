# *args和**kwargs主要用于函数定义，比如写函数装饰器时，也可以用来做猴子补丁（monkey patching，在程序运行时修改某些代码）

"""
*args 是用来发送一个非键值对的可变数量的参数列表给一个函数（预先不知道函数使用者会传递多少个参数给函数）
"""
def test_args(foo, *args):
    print('The first arg is ', foo)
    for arg in args:
        print('another arg: ', arg)


# test_args('yuefen', 'qiyue', 'bayue', 'jiuyue')

"""
**kwargs 允许将不定长度的键值对参数传递给函数
"""
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


# test_kwargs(name='qiyue')


"""
使用*args和**kwargs调用一个函数
"""
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

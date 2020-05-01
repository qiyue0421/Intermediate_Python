# 装饰器是修改其他函数的功能的函数，有助于简化代码


"""1、一切皆对象
def hi(name='qiyue'):
    return "hi " + name


print(hi())

greet = hi  # 将函数赋值给变量

print(greet())

del hi  # 删除旧函数
# print(hi())  # NameError
print(greet())
"""


"""2、在函数中定义函数
def say_hi(name='qiyue'):
    print("Now, you are inside the say_hi() function")

    def greet():
        return "Now, you are in the greet() function"

    def welcome():
        return "Now, you are in the welcome() function"

    print(greet())
    print(welcome())
    print("Now, you are back in the say_hi() function")


say_hi()
# 上面展示了无论何时调用say_hi()，greet()和welcome()将会被同时调用，且内部两个函数在say_hi()函数之外是不能访问的
"""


"""3、从函数中返回函数
def say_hi(name='qiyue'):
    def greet():
        return "Now, you are in the greet() function"

    def welcome():
        return "Now, you are in the welcome() function"

    if name == 'qiyue':
        return greet
    else:
        return welcome


a = say_hi()
print(a)  # <function say_hi.<locals>.greet at 0x000001F2875EB620> 指向了greet函数
print(a())

b = say_hi('bayue')
print(b)  # <function say_hi.<locals>.welcome at 0x00000237BAD1B730> 指向了welcome函数
print(b())
"""


"""4、将函数作为参数传给另一个函数
def say_hi():
    return "hi qiyue"

def hi(func):
    print("hi")
    print(func())


hi(say_hi)
"""


"""5、第一个装饰器
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()  # 封装一个函数，并修改它的行为

        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove")


a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()
"""


"""6、使用@符号
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()  # 封装一个函数，并修改它的行为

        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove")


a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)  # wrapTheFunction，因为函数名和注释文档被重写了
"""


"""7、解决函数名字和文档重写问题
# @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等功能
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()  # 封装一个函数，并修改它的行为

        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove")


print(a_function_requiring_decoration.__name__)
"""


"""8、规范写法
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return "Function is runnning"


can_run = True
print(func())
"""


"""9、使用场景①——授权
# 装饰器有助于检查某个人是否被授权去使用一个web应用的端点，它们被大量使用于Flask和Django web框架中
from functools import wraps
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
"""


"""10、使用场景②——日志
from functools import wraps
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    return x + x


print(addition_func(4))
"""


"""11、在函数中嵌入装饰器
from functools import wraps

def logit(logfile='out.log'):  # 创建一个包裹函数，指定一个用于输出的日志文件
    def logging_decorator(func):  # 装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现将日志打印到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator


@logit()
def myfun1():
    pass


myfun1()

@logit(logfile='func2.log')
def myfunc2():
    pass


myfunc2()
"""


"""12、使用类装饰器类
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__  + "  was called"
            print(log_string)
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass


@logit()
def myfunc1():
    pass


myfunc1()

# 创建logit子类，添加email功能
class email_logit(logit):
    def __init__(self, email='qiyue0421@qq.com', *args, **kwargs):
        self.email = email
        super(logit, self).__init__(*args, **kwargs)

    def notify(self):
        pass
"""

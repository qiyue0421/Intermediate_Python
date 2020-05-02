# try/except基本语句处理异常
# 例子，处理文件IO异常
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred: {}'.format(e.args[-1]))


# 处理多个异常
# 方法1：把所有可能发生的异常放到一个元组里
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print('An IOError occurred: {}'.format(e.args[-1]))

# 方法2：对每个单独的异常在单独的except语句块中处理
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except FileNotFoundError as e:
    print("File not found.")
except IOError as e:
    print("An error occurred.")
    raise e

# 方法3：捕获所有异常
try:
    file = open('test.txt', 'rb')
except Exception as e:
    print('An error occurred: {}'.format(e.args[-1]))


# finally从句：包裹到finally从句中的代码不管异常是否触发都会被执行，可以用来在脚本执行之后做清理工作
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred: {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred.")


# try/else从句
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:  # 这里的代码块只会在try语句没有触发异常时运行，但是这里的异常不会被捕获
    print('This would only run if no exception occurs.')
finally:
    print('This would be printed in every case.')

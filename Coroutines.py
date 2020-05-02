# python中的协程和生成器很相似但又稍有不同，主要区别在于：生成器是数据的生产者，协程是数据的消费者
def grep(pattern):
    print('Searching for', pattern)
    while True:
        line = (yield)  # yield变成了协程，不再包含任何初始值，相反要从外部使用send()方法传值给它
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)  # 使用next()方法启动协程，执行yield表达式
search.send("I love you")
search.send("Don't you love me")
search.send("I love coroutine instead!")
search.close()  # 调用close()方法关闭一个协程

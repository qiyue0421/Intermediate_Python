"""1、return与global"""
# 函数将两个值作为输入，然后输出它们相加之和
def add(value1, value2):
    return value1 + value2


result = add(3, 5)
print(result)

# 另一种写法
def add1(value1, value2):
    global result1  # 全局变量result1，意味着可以在函数以外的区域访问这个变量
    result1 = value1 + value2


add1(2, 5)
print(result1)
# 实际编程时，应该试着避开global关键字，它只会让生活变得更艰难，因为它引入了多余的变量到全局作用域了


"""2、多个return值"""
# 从一个函数里返回两个变量而不是一个，最著名的方法就是使用global关键字
name = ''
age = 0

def profile():
    global name
    global age
    name = 'qiyue'
    age = 24


profile()
print(name)
print(age)
# 注意：不要试着使用上述方法！不要试着使用上述方法！不要试着使用上述方法！

# 也可以返回一个包含多个值的tuple、list、dict来解决这个问题，是一种可行的方式
def profile1():
    name1 = 'bayue'
    age1 = 29
    return (name1, age1)
    # return name1, age1


profile_data = profile1()
print(profile_data[0], profile_data[1])

# __slots__魔法
# 在python中，每个类都有实例属性，默认情况下，python使用一个字典来保存一个对象的实例属性，这允许我们在运行时去设置任意的新属性，但是对于已知属性的小类来说，
# 可能是个瓶颈，因为这个字典浪费了很多内存

# 可以使用__slots__方法告诉python不要使用字典，而且只给一个固定集合的属性分配空间
# 不使用 __slots__
class MyClass1(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

    def set_up(self):
        pass

# 使用 __slots__
class MyClass2(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

    def set_up(self):
        pass

# 第二段代码会减少内存负担，内存占用率减少40%~50%

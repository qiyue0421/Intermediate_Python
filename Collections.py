# pythonr附带一个模块，它包含许多容器数据类型，名字为collection

"""1、defaultdict
# 与dict类型不同，不需要检查key是否存在
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# 当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发KeyError异常，defaultdict允许我们绕过这个问题
# 问题：
# some_dict = {}
# some_dict['color']['favourite'] = 'yellow'  # 异常输出：KeyError 'colours'

# 解决方案：
import json

tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['color']['favourite'] = 'yellow'
print(json.dumps(some_dict))  # {"color": {"favourite": "yellow"}}
"""


"""2、counter
# Counter是一个计数器，可以针对某项数据进行计数
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

fas = Counter(name for name, colour in colours)
print(fas)
"""


"""3、deque
# deque提供了一个双端队列，可以从头尾两端添加或删除元素
from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')
print(len(d))
print(d)

d = deque(maxlen=30)  # 限制列表大小，当插入超过30条数据时，最左边一端的数据将从队列中删除

d.extendleft([0])  # 从左端扩展数据
d.extend([6, 7, 8])  # 从右端扩展数据
"""


"""4、namedtuple
# 元组是一个不可变的列表，可以存储一个数据的序列，它和命名元组非常像，但有几个关键的不同
# 主要相似点是都不像列表，不能修改元组中的数据，为了获取元组中的数据，需要使用整数作为索引
man = ('Ali', 30)
print(man[0])

# 命名元组把元组变成一个针对简单任务的容器，不必使用整数索引来访问一个命名元组中的数据，可以像字典一样访问数据，但是要始终注意：命名元组还是不可变的
# 命名元组有两个必须的参数，它们是元组名称和字段名称
from collections import namedtuple

animal = namedtuple('Animal', 'name age type')  # 元组名称是Animal，字段名称是"name"、"age"和"type"
perry = animal(name="perry", age=31, type="cat")
print(perry)  # Animal(name='perry', age=31, type='cat')
print(perry.name, perry.age, perry.type)  # 使用名称访问命名元组

print(perry._asdict())  # 将命名元组转换为字典
"""


"""5、枚举 Enumerate
# 枚举（enumerate）是python内置函数
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
some_list = [1, 2, 3, 1, 2, 4, 5, 6]
for count, value in enumerate(some_list):
    print(count, value)

print()
for count, value in enumerate(some_list, 1):  # 可选参数指定从哪个数据开始枚举
    print(count, value)

# 创建包含索引的元组列表
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
"""

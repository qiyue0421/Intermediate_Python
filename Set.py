"""1、set（集合）数据结构"""
# set是一个非常有用的数据结构，它与列表的行为类似，区别在于set不能包含重复的值


# 例如，检查列表中是否包含重复的元素
# 方法1：for循环
list1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in list1:
    if list1.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# 方法2：set实现去重
list2 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

result = set([x for x in list2 if list2.count(x) > 1])
print(list(result))


# 交集：两个集合中都有的数据
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
print((input_set.intersection(valid)))


# 差集：找出无效的数据，相当于用一个集合减去另一个集合的数据
print(input_set.difference(valid))

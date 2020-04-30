from Debuging.test2 import *

def test1_function1(list1, list2):
    content1 = "Test1 Function1 List1"
    list1.append(content1)
    content2 = "Test1 Function1 List2"
    list2.append(content2)

    test2_function1(list1, list2)

    finish_content = "Test1 Function1 Finished"
    list1.append(finish_content)
    list2.append(finish_content)


def test1_function2(list1, list2):
    test1_function1(list1, list2)

    content1 = "Test1 Function2 List1"
    list1.append(content1)
    content2 = "Test1 Function2 List2"
    list2.append(content2)

    finish_content = "Test1 Function2 Finished"
    list1.append(finish_content)
    list2.append(finish_content)


if __name__ == '__main__':
    list1 = ["List1 Main"]
    list2 = ["List2 Main"]
    test1_function2(list1, list2)
    print(list1)
    print(list2)
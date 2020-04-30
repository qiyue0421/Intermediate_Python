def test2_function1(list1, list2):
    content1 = "Test2 Function1 List1"
    list1.append(content1)
    content2 = "Test2 Function1 List2"
    list2.append(content2)

    loop_test(list1, list2)

    finish_content = "Test2 Function1 Finished"
    list1.append(finish_content)
    list2.append(finish_content)

def loop_test(list1, list2):
    for i in range(5):
        list1.append(i)
        list2.append(i)

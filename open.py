# open函数可以打开一个文件

"""1、演示一个使用错误的做法：
f = open('photo.jpg', 'r+')  # open的返回值时一个文件句柄，从操作系统托付给python程序，一旦处理完文件，需要归还这个文件句柄（这样不会超出一次能打开的文件句柄的数量上限）
jpgdata = f.read()  # 显示的调用close关闭了这个文件句柄
f.close()  # 但前提是只有在read成功的情况下，如果有执行过程中有任何异常产生，close将不会被调用
"""


"""2、为了确保不管异常是否触发，文件都能关闭，可以将其包裹成一个with语句
# open的第一个参数是文件名，第二个参数是打开模式，决定了这个文件如何被打开
# - 如果是读取文件，传入 r
# - 如果是读取二进制文件，传入 rb
# - 如果是读取并写入文件，传入 r+
# - 如果是覆盖写入文件，传入 w
# - 如果是在文件末尾附加内容，传入 a
with open('photo.jpg', 'r+') as f:
    jpgdata = f.read()
"""


"""3、读取一个文件并检测是否是JPG格式
import io
with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):  # 文件格式以 FF D8 开始
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))
"""


"""4、基于类实现上下文管理器"""
# 一个上下文管理器的类，最起码要定义__enter__和__exit__方法
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')

'''底层发生的事情
1、with语句先暂存了File类的__exit__方法
2、然后它调用File类的__enter__方法
3、__enter__方法打开文件并返回给with语句
4、打开的文件句柄被传递给opened_file参数
5、使用write()方法写文件
6、with语句调用之前暂存的__exit__方法
7、__exit__方法关闭了文件
'''

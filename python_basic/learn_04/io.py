import json
import os
import pickle
from io import StringIO, BytesIO

"""
IO在计算机中指Input/Output，也就是输入和输出
Python的IO编程接口
"""

# 文件读写：读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的
# 打开文件：使用Python内置的open()函数，传入文件名和标示符
try:
    f = open('D:/Python/test.txt', 'r', errors='ignore')
# 文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    str = f.read()
    print(str)  # Hello, World!
finally:
    if f:
        f.close()  # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源

# 上述写法每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open('D:/Python/test.txt', 'r') as f:
    print(f.read())  # Hello, World!

# 调用read()会一次性读取文件的全部内容，保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
# 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list

# file-like Object:像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object

# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
with open('E:\\image\\tom.jpg', 'rb') as f:
    print(f.read())

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数; open('', 'r', encoding='gbk')
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError;open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理
# open('', 'r', encoding='gbk', errors='ignore')

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('D:/Python/test.txt', 'w')
f.write('hello Python')
f.close()
# 务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘
# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）;可以传入'a'以追加（append）模式写入
with open('D:/Python/test.txt', 'a') as f:
    f.write('hello World!')

# StringIO:在内存中读写str,要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
f = StringIO()
f.write('hello, Python')
f.write(' ')
f.write('hello, world')
print(f.getvalue())  # hello, Python hello, world  getvalue()方法用于获得写入后的str

# 用一个str初始化StringIO，然后，像读文件一样读取
f = StringIO('hello\nworld\npython')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 写入的不是str，而是经过UTF-8编码的bytes
print(f.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口


"""
在Python程序中执行这些目录和文件的操作:Python内置的os模块也可以直接调用操作系统提供的接口函数
"""

print(os.name)  # 操作系统类型 nt: windows
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中
print(os.environ)  #
print(os.environ.get("PATH"))  # 获取某个环境变量的值

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print(os.path.abspath('.'))  # 获取当前目录的绝对路径  D:\Python\program\firstPythonProject\python_basic\learn_04

# 利用Python的特性来过滤文件
# 获取当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])  # []
# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])  # ['io.py', '__init__.py']


"""
把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
    序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
Python提供了pickle模块来实现序列化
"""

# 把一个对象序列化，并写入文件中
d = dict(name='tom', age=20, score=80)
print(pickle.dumps(d))  # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
f = open('D:/Python/dump.txt', 'wb')
pickle.dump(d, f)  # pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()

# 读取并反序列化
f = open('D:/Python/dump.txt', 'rb')
d = pickle.load(f)  # 用pickle.load()方法从一个file-like Object中直接反序列化出对象
print(d)  # {'name': 'tom', 'age': 20, 'score': 80}

"""
在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
"""

print(json.dumps(d))  # {"name": "tom", "age": 20, "score": 80}  dumps()方法返回一个str，内容就是标准的JSON


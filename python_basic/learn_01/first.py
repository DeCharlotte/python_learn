'''
这是多行注释
'''
# num1 = int(input('请输入一个数字：'))
# num2 = int(input('请输入一个数字：'))
# sum = num1 + num2
# # 这是一个单行注释
# print('两数之和：', sum)
# 转义字符\
print('I\'m \"OK\"')
# r''表示''内部的字符不转义
print(r'\\\t\\')
# 布尔值 True False
print(3 > 2)
print(True and False)  # False
print(True or False)  # True
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('adult')
else:
    print('teenager')
# 空值None
# 变量:变量本身类型不固定的语言称为动态语言
a = 12  # a是一个整数
print(a)
b = a  # 变量b指向变量a指向的数据
a = 'ABC'  # a变为一个字符串
print(a)  # 'ABC'
print(b)  # 12
# 常量
PI = 3.1415926
# 除法运算 /:结果为浮点数  //地板除法：只去结果的整数部分
print(10 / 3)  # 3.3333333333333335
print(10 // 3)  # 3
print(9 / 3)  # 3.0
# 取余
print(10 % 3)  # 1

# 字符串 编码 解码 Unicode UTF-8
# ord():获取字符的整数表示
# chr():把编码转化为对应的字符
print(ord('A'))  # 65
print(ord('中'))  # 20013
print(chr(66))  # B
print(chr(25991))  # 文
''' Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
'''
# encode():将字符串编码为指定bytes
# 'ABC' 和 b'ABC' 内容一样，但是 bytes 的每个字符都只占用一个字节
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
'''
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
'''
print(b'ABC'.decode('ascii'))  # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
# bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xe6'.decode('utf-8', 'ignore'))
# len():计算字符数
print(len('ABC'))  # 3
print(len('中文'))  # 2
# 字符转化为bytes,len()就变为求字节长度
print(len(b'ABC'))  # 3
print(len('中文'.encode('utf-8')))  # 6  1个中文字符经过UTF-8编码后通常会占用3个字节
# 格式化字符串 %d %s %f %x  是否补0和整数与小数的位数
print('%.2f' % PI)  # 3.14
print('%2d-%02d' % (3, 1))  # 3-01
print('age: %s; gender: %s' % (25, True))  # 不知道具体类型，使用%s即可，会将其他类型转化为str
print('growth-rate: %.3f%%' % PI)  # 用%对%转义
# 格式化字符串：format()  占位符{0}、{1}...
print('hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125))

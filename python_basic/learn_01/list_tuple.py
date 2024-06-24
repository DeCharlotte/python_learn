'''
Python内置的一种数据类型是列表：list  []。list是一种有序的集合，可以随时添加和删除其中的元素。
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)  # ['Michael', 'Bob', 'Tracy']
print(len(classmates))  # 3
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])  # Michael
print(classmates[-1])  # Tracy  -1 最后一个元素
print(classmates[-2])  # Bob  -2:倒数第二个元素  -3...
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Jack')
classmates.pop()  # 删除末尾元素
classmates.pop(1)  # 删除指定位置元素, i为索引位置
# 元素插入指定位置, i为索引位置
classmates.insert(1, 'Adam')
classmates.reverse()  # 翻转
# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
R = ['python', 'java', ['aop', 'ioc'], 'scheme']
print(len([]))  # 0
'''
另一种有序列表叫元组：tuple  ()。tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
你可以正常地使用classmates[0],但不能赋值成另外的元素;代码更安全。如果可能，能用tuple代替list就尽量用tuple
'''
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t = ()  # 空tuple
print(t)  # ()
t = (1)  # 表示定义1这个数
print(t)  # 1  括号()既可以表示tuple，又可以表示数学公式中的小括号
t = (1,)  # 表示定义定义只有一个元素的tuple
print(t)  # (1,)
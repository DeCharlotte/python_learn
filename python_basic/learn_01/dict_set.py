'''
Python内置了字典：dict的支持，dict全称dictionary，
在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

dict的key必须是不可变对象,这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）
在Python中，字符串、整数等都是不可变的，因此，可以作为key。而list是可变的，就不能作为key
'''
d = {'Micheal':88, 'Bob':70, 'Trace':58}
print(d['Micheal'])  # 88
d['Adam'] = 79
print(d['Adam'])  # 79
d['Trace'] = 80
# 判断key是否在d中
print('Tom' in d) # False
print(d.get('Thomas'))  # None
print(d.get('Thomas', -1))  # 自己指定的value: -1
print(d.pop('Bob'))  # 删除key, 返回value:70
print(d)

'''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
要创建一个set，需要提供一个list作为输入集合
'''
s = set([1,2,3])  # 传入的list只是告诉set有1,2,3这三个元素，其顺序也不表示set是有序的，重复元素在set中自动被过滤
print(s)  # {1, 2, 3}
s.add(4)  # 田间元素
print(s)  # {1, 2, 3, 4}
s.remove(4)  # 删除元素
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)  # 相交 {2, 3}
print(s1 | s2)  # 相并 {1, 2, 3, 4}
# 不能add可变元素，如list, 最常用的key是字符串
# s.add([1,2])  # TypeError: unhashable type: 'list'
s.add((1,))
print(s)

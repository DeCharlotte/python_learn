'''
Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
'''
names = ['Micheal', 'Bob', 'Trace']
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
for name in names:
    print(name)

# 计算1-10整数之和
sum = 0
for num in [1,2,3,4,5,6,7,8,9,10]:
    sum += num
print(sum)  # 55
# range():生成一个整数序列 list():将range()转化为list列表
print(list(range(5)))  # [0,1,2,3,4]  range(5)生成的序列是从0开始小于5的整数
# 计算1-100的和
sum = 0
for num in range(101):  # [0...100]
    sum += num
print(sum)  # 5050

''''
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
'''
# 计算1-100内所有奇数之和
odd = 0
num = 1
while(num <= 100):
    if num % 2 == 1:
        odd += num
    num = num + 2
print(odd)  # 2500

# 在循环中，break语句可以提前退出循环;也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环

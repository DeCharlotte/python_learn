import unittest
from mydict import Dict
"""
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
    以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    对每一类测试都需要编写一个test_xxx()方法
"""


class TestDict(unittest.TestCase):

    def setUp(self):  # 调用测试方法前被执行
        print('setUp...')

    def tearDown(self):  # 调用测试方法后执行
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, test='value')
        self.assertEqual(d.a, 1)  # # 断言结果与1相等
        self.assertEqual(d.test, 'value')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 期待抛出指定类型的Error
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()

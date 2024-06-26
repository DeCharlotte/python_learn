import sys

"""
模块-module:为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，
    很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）
模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
创建自己的模块时，要注意：
    模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
    模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，
        若成功则说明系统存在此模块。

使用模块:Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用

作用域:在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
在Python中，是通过_前缀来实现private
    正常的函数和变量名是公开的（public）
    类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
    类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

通过pip安装第三方模块，如Numpy;也可以自定义模块，如hello.py
"""

print(sys.path)

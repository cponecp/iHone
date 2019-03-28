"""
导入总是位于文件的顶部，在模块注释和文档字符串之后，在模块的全局变量与常量之前。
导入应该按照以下顺序分组：

标准库导入
相关第三方库导入
本地应用/库特定导入
你应该在每一组导入之间加入空行。

"""
from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c'] # __all__只能影响到 from import * 这种import 方式, 对于from import 的 import 方式没有影响。
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys


def long_function_name(*args):
    pass


var_one = var_two = var_three = var_four = 1
# 与左括号对齐
foo = long_function_name(var_one, var_two,
                         var_three, var_four)


# 用更多的缩进来与其他行区分
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# 挂行缩进应该再换一行
foo1 = long_function_name(
    var_one, var_two,
    var_three, var_four)

# 挂行缩进不一定要用4个空格
foo2 = long_function_name(
    var_one, var_two,
    var_three, var_four)


with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())


# 推荐：运算符和操作数很容易进行匹配
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

ham = []
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


def munge(input: AnyStr, sep: AnyStr = None, limit=1000):
    pass

# 当检查一个对象是否为string类型时，记住，它也有可能是unicode string！在Python2中，str和unicode都有相同的基类：basestring，所以你可以这样：
str
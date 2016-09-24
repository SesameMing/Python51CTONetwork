#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-24 11:13
"""
一个计算器的作业
"""
import re

def compute_jj():
    """
    计算加减
    :return:
    """


def compute_cc():
    """
    计算乘除
    :return:
    """
    pass


def compute(formula):
    """
    计算值
    :return: 计算括号里的值
    """
    r = re.search('[*/]', formula, 1).group()
    print(r)
    # return eval(result)


def parentheses(formula):
    """
    处理括号
    :return: 返回最后的结果
    """
    while True:
        result = re.split(r"\(([0-9*\/+\-\.]+)\)", formula, 1)
        if len(result) == 1:
            break
        result[1] = str(compute(result[1]))
        formula = ''.join(result)
    result = compute(result[0])
    return result


def main():
    # formula = input("请输入计算公式：")
    formula = '1+1+(1+1-1*1+(1/1+1-1*1))+(1+1)+1*1'
    # print(eval(formula))
    formula = re.sub("\s*", "", formula)
    num = parentheses(formula)
    print(num)


if __name__ == '__main__':
    main()

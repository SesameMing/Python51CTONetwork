#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-09-24 11:13
"""
一个计算器的作业
"""
import re


def __replace_sign():
    pass


def compute_jj(arg):
    """
    计算加减
    :return:
    """
    # 处理存在多个符号问题
    while True:
        if arg[0].find('--') != -1 or arg[0].find('-+') != -1 or arg[0].find('++') != -1 or arg[0].find('+-') != -1:
            arg[0] = arg[0].replace('+-', '-')
            arg[0] = arg[0].replace('++', '+')
            arg[0] = arg[0].replace('-+', '-')
            arg[0] = arg[0].replace('--', '+')
        else:
            break

    # 处理以-号开头的公式 类似 -1+3
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-', '&')
        arg[0] = arg[0].replace('+', '-')
        arg[0] = arg[0].replace('&', '+')
        arg[0] = arg[0][1:]

    val = arg[0]
    mch = re.search('\d+\.*\d*[+\-]\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('\d+\.*\d*[+\-]\d+\.*\d*', val).group()
    # print(content)
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)

    before, after = re.split('\d+\.*\d*[+\-]\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    compute_jj(arg)


def compute_cc(arg):
    """
    计算乘除
    :return:
    """
    val = arg[0]
    number = re.search("\d+\.*\d*[*/]+[+\-]?\d+\.*\d*", val)
    if not number:
        return
    content = re.search('\d+\.*\d*[*/]+[+\-]?\d+\.*\d*', val).group()
    if len(content.split("*")) > 1:
        n1, n2 = content.split("*")
        value = float(n1) * float(n2)
    elif len(content.split("/")) > 1:
        n1, n2 = content.split("/")
        value = float(n1) / float(n2)

    before, after = re.split('\d+\.*\d*[*/]+[+\-]?\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    compute_cc(arg)


def compute(formula):
    """
    计算值
    :return: 计算括号里的值
    """
    inp = [formula, 0]
    compute_cc(inp)
    compute_jj(inp)

    # 处理在加减法中 以-开头的公式
    if divmod(inp[1], 2)[1] == 1:
        result = float(inp[0])
        result = result * -1
    else:
        result = float(inp[0])
    return result


def parentheses(formula):
    """
    处理括号
    :return: 返回最后的结果
    """
    while True:
        result = re.split(r"\(([0-9*/+\-.]+)\)", formula, 1)

        if len(result) == 1:
            break
        result[1] = str(compute(result[1]))
        formula = ''.join(result)
        print(formula)
    result = compute(formula)
    return result


def main():
    # formula = input("请输入计算公式：")
    formula = '-0.2*0.22-(3.3/23.5-22*23)+2*(1-(1.3*(2/25-2*(2.3-1))))'
    # print(eval(formula))
    formula = re.sub("\s*", "", formula)  # 替换掉输入中的空格
    num = parentheses(formula)
    print("您的计算结果是：", num)
    print("另一种计算结果验证：", eval(formula))


if __name__ == '__main__':
    main()


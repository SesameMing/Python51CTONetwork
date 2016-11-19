#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time:2016-10-01 15:38
import sys
import time
from modules.lib import Gaofushuai, Diaosi, Meinv


def main():
    John = Diaosi.Diaosi('John', '男', '18', '学生', '黄种人', '中国', '编程', 1000, 0, 0)
    Liz = Meinv.Meinv('Liz', '女', '18', '学生', '黄种人', '中国', '逛街，购物', 1000, 0, 0)
    Peter = Gaofushuai.Gaofushuai('Peter', '男', '18', '富二代', '黄种人', '中国', '泡妞', 2000000, 0, 0)
    print("故事背景：屌丝John，美女Liz，高富帅Peter。")
    John.rwjs()
    Liz.rwjs()
    Peter.rwjs()
    print("时间：上大学期间")
    print("John和Liz每天一同上课，自习，慢慢的，John对Liz产生了爱慕之情。")
    while True:
        John_CHOOSE = input("John 是否向Liz表白（y:是<推荐>, n:否）>>>:")
        if John_CHOOSE == 'y':
            print("Petter 向Liz表白")
            Liz_CHOOSE = input("Liz是否同意Petter的表白（y:是<推荐>, n:否）>>>:")
            if Liz_CHOOSE == 'y':
                print("John和Liz成为了恋人")
                John.tanlianai(Liz)
                break
            else:
                print("John 你被Liz 拒绝了，从此一蹶不振，游戏结束，Game Over")
                exit(0)
        else:
            print("John都不表白，注定孤独一生，游戏结束，Game Over")
            exit(0)
    print("时间过的很快，转眼毕业了，")
    print("Liz遇到了Peter，Perter是个富二代高富帅，家里有钱")
    Liz_CHOOSE = input("Liz是否选择劈腿和Peter在一起？（y:是, n:否）>>>:")
    while True:
        if Liz_CHOOSE == 'y':
            Liz.pitui(Peter)
            break
        elif Liz_CHOOSE == 'n':
            print("Liz下决心和John好好在一起")
            break

    if John.duixiang is None:
        print("Liz的离开，John非常的伤心")
        str1 = """
面对这样的情况,请帮John选择
1.奋发图强
2.沉沦
            """
        print(str1)
        while True:
            John_CHOOSE = input(">>>:")
            if John_CHOOSE == '1':
                John.nuli()
                break
            elif John_CHOOSE == '2':
                John.buwuzhengye()
                break

        if int(John.money) <= 0:
            print("John,穷困撂倒，一分钱都不剩了，从此一蹶不振，孤独到老 Game Over")
            exit(0)
        elif int(John.money) >= 100000:
            print("John通过自己的努力，已经有了存款%s, 车：%s辆， 房：%s栋" % (John.money, John.che, John.fang))
            Peter.fenshou()
            print("Liz 找 John复合")
            print("而Jhon却说：")
            str1 = """
1.当初抛下我，现在又来找我？我不要复合。
2.嗯，我还在等你。
            """
            print(str1)
            John_CHOOSE = input(">>>:")
            while True:
                if John_CHOOSE == '1':
                    print('"当初抛下我，现在又来找我？我不要复合."')
                    print("从此，Jhon在事业上一路高歌，更遇到自己的知心爱人,圆满结束。")
                    break
                elif John_CHOOSE == '2':
                    print('".嗯，我还在等你。"')
                    John.tanlianai(Liz)
                    print("Jhon 和 Liz又走到了一起。开始了新的生活, 结束")
                    break

    else:
        """ Liz 没有和 John分手"""
        print("Liz 和 John没有分手，即将毕业，Jhon开始")
        str1 = """
        面对这样的情况,请帮John选择
1.奋发图强找工作
2.沉沦生活,无心奋斗
            """
        print(str1)
        while True:
            John_CHOOSE = input(">>>:")
            if John_CHOOSE == 1:
                John.nuli()
                break
            elif John_CHOOSE == 2:
                John.buwuzhengye()
                break

        if int(John.money) <= 0:
            print("John,不务正业，穷困撂倒，一分钱都不剩了，Liz也离开了他，从此一蹶不振，孤独到老 Game Over")
            exit(0)
        elif int(John.money) >= 100000:
            print("John通过自己的努力，已经有了存款%s, 车：%s辆， 房：%s栋" % (John.money, John.che, John.fang))
            print("从此John和Liz过上了幸福生活。")


def run():
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/11/23 21:35
# @Author: Ginkgo
# @File :ff.py

def Login(uname, pwd):
    """
    :param uname: 输入用户名
    :param pwd: 输入密码
    :return: "如果用户名和密码都正确，那么返回True,否则返回False
    """
    with open("db", "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip().split(":")
            if line_list[0] == uname and line_list[1] == pwd:
                return True

    return False


def register(uname, pwd):
    """
    注册新用户
    :param uname: 用户名
    :param pwd: 密码
    :return: 注册成功返回True
    """
    if is_exist(uname):
        return False
    with open("db", "a", encoding="utf-8") as f:
        f.write("\n" + uname + ":" + pwd)
        return True


def is_exist(uname):
    """
    验证用户是否存在
    :param uname: 用户名
    :return: 如果存在，返回Ture
    """
    with open("db", "r", encoding="utf-8") as f:
        for line in f:
            if uname == line.strip().split(":")[0]:
                return True
    return False
def chpwd(uname, pwd):
    """
    修改密码
    :param uname: 输入用户名
    :param pwd: 输入密码
    :return:  如果用户名，密码输入正确，进行修改，返回True
    """
    with open("db", "r+", encoding="utf-8") as f:
        lines = 0
        nline = ""
        for line in f:
            # print(f.tell())
            lines = lines +1
            line_list = line.strip().split(":")
            if line_list[0] == uname and line_list[1] == pwd:
                npwd1 = input("请输入新密码：")
                npwd2 = input("请重新输入密码：")
                if npwd1 == npwd2:
                    # f.write()
                    # line.replace(line_list[1], npwd1)
                    nline = uname + ":" + npwd1 + "\n"
                    # f.seek()
                    # f.truncate()
                    # f.write(line)
                    print(lines)

                    return True
    with open("db", "r+") as f1:
        f1.readlines(lines-1)
        f1.seek(0)
        # f1.writelines(nline)






def main():
    print("欢迎使用银杏系统！")
    inp = input("注册用户请按1，登录请按2 ，查询请按3,修改密码请按4：")
    if inp == "1":
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if register(username, password):
            print("注册成功")
        else:
            print("注册失败")

    if inp == "2":
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if Login(username, password):
            print("登录成功")
        else:
            print("登录失败")
    if inp == "3":
        username = input("请输入用户名：")
        if is_exist(username):
            print("该用户存在")
        else:
            print("该用户不存在")
    if inp == "4":
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if chpwd(username, password):
            print("密码修改成功")
        else:
            print("密码修改失败")

main()

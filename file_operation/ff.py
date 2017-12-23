#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author:Ginkgo
# @Time:2017/11/24 0024 11:17
# @File:ff.py

def chpwd(uname,pwd):
    with open("db", "r+", encoding="utf-8") as f1, open("ha", "w+", encoding="utf-8") as f2:
        for line in f1:
            if line.strip().split(":")[0] == uname and  line.strip().split(":")[1] == pwd:
                Npwd1 = input("请输入新密码：")
                Npwd2 = input("请确认密码：")
                if Npwd1 == Npwd2:
                    f2.writelines(uname + ":" + Npwd1 + "\n")
                    return True
            else:
                f2.writelines(line)

chpwd("aab","abb")

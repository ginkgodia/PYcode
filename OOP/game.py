#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: game
# @Time: 2018/1/12 23:39

import pickle,time,subprocess


class exc:
    def back(self):
        print("exec backup.....")
        with open("recod.log", "wb") as f:
            f.write(pickle.dumps())

    def read(self):
        print("Reading recod.....")
        with open("recod.log", "rb") as f:
            r = pickle.loads(f.read())
            return r.role, r.life, r.exp


class game(exc):
    def __init__(self, role, life):
        self.role = role
        self.life = life
        self.exp = 0

    def beated(self):
        self.life -= 2
        self.exp += 1

    def hit(self):
        self.life = self.life + 1
        self.exp += 1


Loader = exc()
ret = subprocess.call("ls", shell=True)
print(ret)
"""
e = Loader.read()
name = input("Please input you role:")
if name == e[0]:
    time.sleep(3)
    exit(0)
else:
    life = "user is not exist ,please input your life:"
    Name = game(name, life)
    print(Name.role)

"""

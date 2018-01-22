#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: Adminstrator
# @Time: 2018/1/18 22:24
import pickle
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
from lib import modules
from conf import setting
from lib.modules import *


def login(username, password):
    if os.path.exists(os.path.join(setting.BASE_ADMIN_DIR, username)):
        ad_obj = pickle.load(open(os.path.join(setting.BASE_ADMIN_DIR, username), "rb"))
        if ad_obj.login(username, password):
            return ad_obj.username
        else:
            return 1
    else:
        print("Error , user not exist")


def register(username, password):
    if os.path.exists(setting.BASE_ADMIN_DIR, username):
        print("The user exist")
    else:
        ad1 = modules.Admin()
        ad1.register(username, password)


def create_teacher(admin):
    teacher_list = []
    while True:
        name = input("Please input teacher name,and input Q/q to quit:")
        if name.lower() == "q":
            if os.path.exists(setting.TEACHER_DB_DIR):
                exist = pickle.load(open(setting.TEACHER_DB_DIR, "rb"))
                teacher_list.extend(exist)
            pickle.dump(teacher_list, open(setting.TEACHER_DB_DIR, "wb"))
            break
        else:
            age = input("Please input teacher age:")
            teacher = modules.Teacher(name, age, admin)
            teacher_list.append(teacher)


def create_course(admin):
    course_list = []
    teacher_list = pickle.load(open(setting.TEACHER_DB_DIR, "rb"))
    for num, teacher in enumerate(teacher_list, 1):
        print(num, teacher.name, teacher.create_admin, teacher.create_time)
    while True:
        course = input("Please input course name,and input Q/q to quit:")
        if course.lower() == "q":
            if os.path.exists(setting.COURSE_DB_DIR):
                exist = pickle.load(open(setting.COURSE_DB_DIR, "rb"))
                course_list.extend(exist)
            pickle.dump(course_list, open(setting.COURSE_DB_DIR, "wb"))
            break
        else:
            cost = input("Please input course cost:")
            teacher_num = int(input("Please input course teacher:"))-1

        course_obj = modules.Course(course, cost, teacher_list[teacher_num], admin)
        course_list.append(course_obj)


def main():
    inp = input("Please input your choice: 1,register 2,login\n >>>>")
    username = input("Please input your name:")
    password = input("Please input your pwd:")
    if inp == "1":
        register(username, password)
    elif inp == "2":
        ret = login(username, password)
        if ret:
            print("login success")
            sel = input("1,创建老师；2,创建课程\n >>>>")
            if sel == "1":
                create_teacher(ret)
            if sel == "2":
                create_course(ret)
        elif ret == 1:
            print("Password error")

        else:
            print("Error")
    else:
        print("error")


if __name__ == '__main__':
    main()

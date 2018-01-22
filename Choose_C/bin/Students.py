#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: Students
# @Time: 2018/1/18 22:37

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.modules import *
from conf import setting
import pickle
def login(username, password):
    if os.path.exists(os.path.join(setting.BASE_STUDENT_DIR, username)):
        st_obj = pickle.load(open(os.path.join(setting.BASE_STUDENT_DIR, username), "rb"))
        if st_obj.login(username, password):
            return st_obj
        else:
            return 1
    else:
        print("Error , user not exist")

def register(user, pwd):
    st1 = Student()
    st1.register(user, pwd)

def choose_course(st_obj):
    course_list = pickle.load(open(setting.COURSE_DB_DIR, "rb"))
    for num, item in enumerate(course_list, 1):
        print(num, item.course, item.cost, item.teacher.name)

    while True:
        num = input("input you course num ,'q/Q ' to quit:")
        if num.lower() == "q":
            # if os.path.exists(os.path.join(setting.BASE_STUDENT_DIR, st_obj.name)):
            #     exist = pickle.load(open(setting.BASE_STUDENT_DIR, "rb"))
            #     st_obj.Course_list.extend(exist)
            pickle.dump(st_obj, open(os.path.join(setting.BASE_STUDENT_DIR, st_obj.name), "wb"))
            break
        course = int(num)-1
        # print(course_list[course], st_obj.Course_list)
        # for item in st_obj.Course_list
        # if course_list[course].course not in st_obj.Course_list:
        st_obj.Course_list.add(course_list[course])
        # st_obj.Course_list = set()
def course_info(st_obj):
    # st_objpickle.load(open(os.path.join(setting.BASE_STUDENT_DIR, st_obj.name), "rb"))
    for item in st_obj.Course_list:
        print(item.course)

def main():
    inp = input("1,login; 2,register \n >>>>" )
    user = input("Your name:")
    pwd = input("Your pwd:")
    if inp == "1":
        ret = login(user, pwd)
        num = input("1.choose course; 2.study course; 3.course info")
        if num == "1":
            choose_course(ret)
        elif num == "2":
            pass
        elif num == "3":
            course_info(ret)
        else:
            pass
    if inp == "2":
        register(user, pwd)
if __name__ == '__main__':
    main()
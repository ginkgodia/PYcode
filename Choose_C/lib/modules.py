#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: modules
# @Time: 2018/1/21 19:08

import pickle
import time
import os, sys
import random
from conf import setting

class Teacher:
    def __init__(self, name, age, admin):
        self.name = name
        self.age = age
        self.__assert = 0
        self.create_time = time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime())
        self.create_admin = admin

    def gain(self):
        pass

class Course:
    def __init__(self, course, cost, teacher, admin):
        self.course = course
        self.cost = cost
        self.teacher = teacher
        self.create_time = time.strftime('%Y-%m-%d  %H:%M:%S')
        self.create_admin = admin


class Admin:
    def __init__(self):
        self.username = None
        self.pwd = None

    def login(self, username, pwd):
        if self.username == username and self.pwd == pwd:
            return True
        else:
            return False

    def register(self, username, pwd):
        self.username = username
        self.pwd = pwd
        path = os.path.join(setting.BASE_ADMIN_DIR, self.username)
        pickle.dump(self, open(path, "wb"))

class Student:
    def __init__(self):
        self.name = None
        self.pwd = None
        self.Course_list = set()
        self.Study_list = []
    def login(self, name, pwd):
        if self.name == name and self.pwd == pwd:
            return True
        else:
            return False

    def register(self, name, pwd):
        self.name = name
        self.pwd = pwd
        pickle.dump(self, open(os.path.join(setting.BASE_STUDENT_DIR, name), "wb"))


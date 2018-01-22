#!/usr/bin/env python
# -*- coding=utf8 -*-

# @Author:Ginkgo
# @File: setting.py
# @Time: 2018/1/21 19:49

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_ADMIN_DIR = os.path.join(BASE_DIR, "db", "admin")
BASE_STUDENT_DIR = os.path.join(BASE_DIR, "db", "student")
TEACHER_DB_DIR = os.path.join(BASE_DIR, "db", "teacher_file")
COURSE_DB_DIR = os.path.join(BASE_DIR, "db", "course_file")
LOG_DIR = os.path.join(BASE_DIR, "logs")
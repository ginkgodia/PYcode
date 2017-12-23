#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2017/12/16 9:47
# @Author: Ginkgo
# @File :pickle_module.py
import pickle



account = {
    '10001': {
        'username': 'qc',
        'passwd': "jindkeen",
        'hk_account': {
            "ICBC": "62179084321111B",
            "CBC": "42318358953"
        },
        'balance': 100000,
        'mails': {
            "qq.mail": "9076329900@qq.com",
            "163.mail": "156893234@163.com"
        }
    },
    '10002': {
        'username': 'qc2',
        'passwd': "jindkeen2",
        'hk_account': {
            "ICBC": "62179084321111B2",
            "CBC": "423183589532"
        },
        'balance': 100000,
        'mails': {
            "qq.mail": "9076329900@qq.com",
            "163.mail": "156893234@163.com"
        }
    }
}
with open('db_name', 'wb') as f:
    f.write(pickle.dumps(account))


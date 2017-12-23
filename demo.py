#!/usr/bin/env python
#-*- coding:utf8
import threading 
import time 
from multiprocessing.dummy import Pool as Threadpool #一个自带的包
#线程池
threading.Thread()
#通过thread来创建线程
def print_hello (name):
	print "hello",name
	time.sleep(2) #延时
name_list =["keli","xiaoxi"] #定义了一个list
start_time = time.time()#导入的方法
pool = Threadpool(1)
'''

'''

pool.map(print_hello,name_list)
pool.close()
pool.join()
'''
主线程等待子线程结束
'''
end_time = time.time()
print "%d second " %(end_time-start_time)

#字符串格式化%d

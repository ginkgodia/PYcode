** subprocess 执行操作系统命令 **

- 执行简单的系统命令：
```python
import subprocess
# 执行系统命令，返回状态码,当shell为False时，系统命令不允许是字符串形形式，必须为列表
# 当shell为True时，系统命令可以是字符串
ret = subprocess.call(["ls", "-a"], shell=False)
ret = subprocess.call("ls -a", shell=True)
# 执行系统命令，如果执行状态码是0，返回0，否则抛出异常
subprocess.check_call("exit -1",shell=True)
"""
result > raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'exit -1' returned non-zero exit status
"""
subprocess.check_call(["ls", "-a"], shell=False)

# 执行命令，如果状态码为0，则返回执行结果，否则抛出异常
subprocess.check_output("exit 1", shell=True)
```

- 执行复杂的系统命令

```python
import subprocess
# subprocess.Popen()
"""
常用参数：
args:shell 命令，可以是字符串或者序列类型(list,tuple)
bufsize: 指定缓冲，0 无缓冲，1 行缓冲，其他缓冲区大小，负值，使用系统缓冲
stdin,stdout,stderr:标准输入，标准输出，错误句柄
preexec_fn:只用于unix平台，用于指定一个可这些对象，在子进程运行之前被调用
close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
shell：同上
cwd：用于设置子进程的当前目录
env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
startupinfo与createionflags只在windows下有效
将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
"""
# subprocess.Popen() 可以处理简单的系统命令，也可以处理复杂的命令
obj = subprocess.Popen("mkdir tt", shell= True,cwd="/root/")
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)
# 可以通过obj.commnuite()方法来简化输出结果
# obj.communicate()可以同时处理标准输出，错误句柄
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')

out_error_list = obj.communicate()
print(out_error_list)
# 如果标准输入较为简单，可以直接通过obj.communicat()执行
out_error_list = obj.communicate('print "hello"')
```
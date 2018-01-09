**shutil是一种高级文件处理模块**

- 对文件进行cp，mv，rm操作
```python
import shutil
# 复制一个文件到另外一个文件，复制对象是类文件对象，也就是说是已经打开的文件，可用进行追加"a" 或 重写"w"
shutil.copyfileobj(open("b.xml", "r"), open("c.xml", "a"))
# 复制一个文件到另一个文件，存在则重写，不存在则创建
shutil.copyfile("b.xml", "c.xml")
# 复制文件的权限，不包括属主和属组及内容
shutil.copymode("a.xml", "b.xml")
# 复制文件的状态信息，包括atime, mtime等
shutil.copystat("a.xml", "b.xml")
# 复制文件和文件的权限
shutil.copy("a.xml", "b.xml")
# 复制文件和文件的状态信息
shutil.copy2("a.xml", "b.xml")
# 递归拷贝目录
shutil.copytree("../request_xml", "test", symlinks=False, ignore=shutil.ignore_patterns("*.pyc", "tmp.*"))
# 递归删除文件
shutil.rmtree("test", ignore_errors=True)
# 递归移动文件
shutil.move("a.xml", "x.xml")
```

- 对文件进行压缩和解压缩操作
```python
import shutil
# shutil.make_archive(basename,format,root_dir,owner,group,logger)
# basename : 压缩包的名称，同样可以是压缩包的路径
# format : 压缩包的种类"zip","tar","bztar","gztar"
# root_dir: 要压缩文件夹的路径
# owner: 用户，默认为当前用户
# group: 组，默认为当前组
# logger: 用于记录日志，通常是logging.logger对象
shutil.make_archive("request", "zip", root_dir="../request_xml/", owner="root", group="root" )
shutil._find_unpack_format("test.zip")
```

- zipfile 和 tarfile
shutil 对压缩包的处理是通过这两个模块实现的

```python
import zipfile
z = zipfile.ZipFile("request.zip","w")
z.write("x.xml")
# z.close()
z.extract("x.xml")
z.extractall()
z.close()
# tarfile 同理
import tarfile
tar = tarfile.open("a.tar", "w")
tar.add("a.xml","arcname")
```
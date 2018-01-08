**configparser模块提供了丰富的处理conf文件的方法**

- 对节点的操作：
```python
import configparser
conf = configparser.ConfigParser()
conf.read("php.ini",encoding="utf-8")
# 审查节点是否存在
has_sec = conf.has_section("name")
# 列出所有节点
secs = conf.sections()
# 添加节点
add_sec = conf.add_section("name2")
conf.write(open("php.ini","w"))
# 删除节点
rem_sec = conf.remove_section("name")
conf.write(open("php.ini","w"))
```

2.对节点下键的操作：
```python
import configparser
conf = configparser.ConfigParser()
conf.read("php.ini",encoding="utf-8")
# 检查节点是否含有指定的键
has_opt = conf.has_option("name1", "k1")
# 列出指定节点下所有的键值对
ls_items = conf.items("name1")
# 获取指定节点下所有的键
ls_opt = conf.options("name1")
# 获取指定节点下所有的key值
K = conf.get("name1","k1")
# 当key值为数字时，可用获得数字格式
K1 = conf.getint("name1", "k1")
K2 = conf.getfloat("name1","k1")
# 删除
rem_opt = conf.remove_option("name1", "k1")
conf.write(open("php.ini","w"))
# 添加
set_opt = conf.set("name1", "k1","v1")
conf.write(open("php.ini","w"))


```
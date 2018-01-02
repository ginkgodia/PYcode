python 有非常多的工具来处理xml

- xml.dom.* 模块 － 是 W3C DOM API 的实现。如果你有处理 DOM API 的需要，那么这个模块适合你。注意：在 xml.dom 包里面有许多模块，注意它们之间的不同。
xml.sax.* 模块 － 是 SAX API 的实现。这个模块牺牲了便捷性来换取速度和内存占用。SAX 是一个基于事件的 API，这就意味着它可以“在空中”(on the fly)处理庞大数量的的文档，不用完全加载进内存
- xml.parser.expat － 是一个直接的，低级一点的基于 C 的 expat 的语法分析器(见注释2)。 expat 接口基于事件反馈，有点像 SAX 但又不太像，因为它的接口并不是完全规范于 expat 库的
- xml.etree.ElementTree (以下简称 ET)。它提供了轻量级的 Python 式的 API ，它由一个 C 实现来提供
**ElementTree 一个API，两种实现**

- 纯python 实现：xml.etree.ElementTree
- C 实现：xml.etree.cElementTree ,尽量使用C语言来实现
- 优先使用cElementTree

```
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
```

在python 3.3之后，py会自动寻找可用的C库来加快速度
xml 是一种分级的数据形式，所以，最自然的表示方法就是将她表示为一个树。ET有两个对象来实现这个目的 

- ElementTree将整个xml解析为一颗数
- Element将单个节点解析为树
如果是整个文档级别的操作，比如读写，查找通常使用ElementTree，单个xml元素和它的子元素通常用Element。
每个Element都有以下属性：

- tag: string 对象，表示数据代表的种类
- attrib: dictionary 对象，表示附有的属性
- text: string 对象，表示element的内容
- tail: string 对象，表示element闭合之后的尾迹

```
<tag attrib1=1>text</tag>tail
  1     2        3         4
```

![xml文件树](http://wiki.jikexueyuan.com/project/start-learning-python/images/22601.jpg)

``` 
<bookstore>
    <book category="COOKING">
        <title lang="en">Everyday Italian</title> 
        <author>Giada De Laurentiis</author> 
        <year>2005</year> 
        <price>30.00</price> 
    </book>
    <book category="CHILDREN">
        <title lang="en">Harry Potter</title> 
        <author>J K. Rowling</author> 
        <year>2005</year> 
        <price>29.99</price> 
    </book>
        <book category="WEB">
        <title lang="en">Learning XML</title> 
        <author>Erik T. Ray</author> 
        <year>2003</year> 
        <price>39.95</price> 
    </book>
</bookstore>
```

``` 
ret = ET.ElementTree(file="doc.xml")
# print(ret)
root = ret.getroot()
print(root.tag, root.attrib)
result > bookstore {}
```

这说明根元素是bookstore，没有属性或者说是空属性
可用使用遍历将其中的所有元素都读出来

``` 
for items in root:
    print(items.tag, items.attrib)
    
result > book {'category': 'COOKING'}
        book {'category': 'CHILDREN'}
        book {'category': 'WEB'}
取出指定元素：
        print(root[0].tag)
        print(root[0].attrib)
        print(root[0].text)
        print("=========")
        print(root[0][0].tag)
        print(root[0][0].attrib)
        print(root[0][0].text)
        print(root[0][1].tag)
result >
        book
        {'category': 'COOKING'}
        　\n
        =========
        title
        {'lang': 'en'}
        Everyday Italian
        author

```
对于ElementTree对象，有一个iter方法可以对指定名称的子节点进行深度优先遍历，如果不指定名字，那么则是把所有的元素都遍历一遍

``` 
for item in root.iter(tag="book"):
    print(item.tag, item.attrib)

for items in root.iter(tag="title"):
    print(items.tag, items.attrib)
    
result >
        book {'category': 'COOKING'}
        book {'category': 'CHILDREN'}
        book {'category': 'WEB'}
        title {'lang': 'en'}
        title {'lang': 'en'}
        title {'lang': 'en'}　
```

除了上述方法，还可以通过路径，搜索到指定内容，读取其内容，即xpath
``` 
for item in root.iterfind("book/title"):
    print(item.tag, item.text)

for items in root.findall("book"):
    title = items.find("title").text
    price = items.find("price").text
    lang = items.find("title").attrib
#    lang = items.find("title").attrib.get("lang")
#    获得属性中key所包含的value
    print(title, price, lang)
    
result > 
        title Everyday Italian
        title Harry Potter
        title Learning XML
        Everyday Italian 30.00 {'lang': 'en'}
        Harry Potter 29.99 {'lang': 'en'}
        Learning XML 39.95 {'lang': 'en'}
```

**Element 对象**

**常用属性：**

```
tag：string，元素数据种类
text：string，元素的内容
attrib：dictionary，元素的属性字典
tail：string，元素的尾形

```

**针对属性的操作**

```
clear()：清空元素的后代、属性、text 和 tail 也设置为 None
get(key, default=None)：获取 key 对应的属性值，如该属性不存在则返回 default 值
items()：根据属性字典返回一个列表，列表元素为(key, value）
keys()：返回包含所有元素属性键的列表
set(key, value)：设置新的属性键与值
```

**针对后代的操作**

```
append(subelement)：添加直系子元素
extend(subelements)：增加一串元素对象作为子元素
find(match)：寻找第一个匹配子元素，匹配对象可以为 tag 或 path
findall(match)：寻找所有匹配子元素，匹配对象可以为 tag 或 path
findtext(match)：寻找第一个匹配子元素，返回其 text 值。匹配对象可以为 tag 或 path
insert(index, element)：在指定位置插入子元素
iter(tag=None)：生成遍历当前元素所有后代或者给定 tag 的后代的迭代器
iterfind(match)：根据 tag 或 path 查找所有的后代
itertext()：遍历所有后代并返回 text 值
remove(subelement)：删除子元素
```

**ElementTree 对象**

```
find(match)
findall(match)
findtext(match, default=None)
getroot()：获取根节点.
iter(tag=None)
iterfind(match)
parse(source, parser=None)：装载 xml 对象，source 可以为文件名或文件类型对象.
write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None,method="xml")　
```

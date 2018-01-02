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


```
<?xml version="1.0"?>
<doc>
    <branch name="testing" hash="1cdf045c">
        text,source
    </branch>
    <branch name="release01" hash="f200013e">
        <sub-branch name="subrelease01">
            xml,sgml
        </sub-branch>
    </branch>
    <branch name="invalid">
    </branch>
</doc>
```


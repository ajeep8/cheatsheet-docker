---
title: markdown进阶
---

# 嵌入md子文档

代码块是markdown最神奇的能力，最开始只是为了文档对代码按代码语法渲染，扩展后就成了非常强大的“活”的部分。

嵌入md子文档可以使大文档结构清晰、方便多人合作写作。

~~~markdown
```include
// 简单嵌入，//是注释
subfile.md
```
~~~

~~~markdown
```{.include shift-heading-level-by=2}
// 嵌入多个子文档并调整目录层级2级：
subfile1.md
sub/subfile2.md
```
~~~

~~~
```include
// 只有注释没有嵌入文档，可以作为md文件的注释用，输出文件不会有注释文字
```
~~~

# 嵌入代码文件

嵌入独立的代码文件，而不是把代码直接写在md文档代码块中，会让主文件更清晰

~~~
```{.c include=test.c caption="嵌入C语言代码"}
这里的文字可选，所有文字被test.c内容替代。
```
~~~

# 内嵌的文本画图

~~~
```mermaid
mermaid画图代码
```
~~~

但mermaid的功能基本被plantuml覆盖，因此建议用PlantUML。

[PlantUML](https://plantuml.com/)不仅是画图，而是UML模型，比图信息更丰富

~~~
```plantuml
@startuml
PlantUML画图代码
@enduml
```
~~~

~~~
```graphviz
digraph finite_state_machine {
  graphviz/dot画图代码
}
```
~~~

python画图有大量的样例代码，想画什么图都可以搜一个类似代码改改数据实现。

~~~
```{.py2image caption="内嵌python画图：Sigmoid"}
import matplotlib.pyplot as plt
...python画图代码
# plt.show()
plt.savefig("$DESTINATION$", dpi=300, format="$FORMAT$")
```
~~~

[Diagrams](https://diagrams.mingrammer.com/)是python做的，可以画很漂亮的系统图。

~~~
```{.py2image caption="内嵌Diagrams图"}
from diagrams import Diagram
......
with Diagram("插图名称", show=False, direction="TB", filename="$DESTINATION$".split(".")[0], outformat="$FORMAT$") as diag:
......
```
~~~

# 引入独立绘图文件

结合嵌入代码文件和文本画图两个能力，可以引用独立画图文件，这样画图文本不必出现在md文件中，更清晰。

~~~
```{.plantuml include=docascode.puml caption="嵌入plantuml图"}
这里的文字可选，所有文字被docascode.puml内容替代，然后渲染成图。
```

```{.graphviz include="linux.gv" caption="嵌入graphviz/dot图" #fig:linux}
这个dot文件比较复杂，所以放独立文件比较干净漂亮。
```

```{.py2image include=matplotlib-test.py caption="嵌入Python画图"}
python画图有大量的样例代码，想画什么图都可以搜一个类似代码改改数据实现。
```

```{.py2image include=diagrams-test.py caption="嵌入Diagrams图"}
Diagrams图也可以用独立py文件嵌入的方法画。
```

```{.drawio include="test.drawio" caption="嵌入draw.io图"}
draw.io是ms visio的开源替代，可以直接嵌入md文件
```
~~~


# csv2table

1. md内嵌csv数据

~~~
```{.table  type="simple" aligns="CR" caption="代码块内嵌" header="yes"}
编号,_是否_
1,**Yes**
2^2^,*No*
**_3_**,Yes
```
~~~

- type：可以是simple、pipe、multiline、grid
- aligns：列对齐字母：R/L/C/D：每列的列对齐方式(R=Right 右，L=Left 左，C=Center 中，D=Default缺省)

2. 引用外部csv文件

将上述语法增加source指出csv文件：

~~~
```{.table  type="simple" aligns="CR" caption="**代码块**引用" source="md0/simple.csv"}
这里的文字导出时没有，可以作为注释
```
~~~

3. 简化语法格式

~~~
![**Simple** _表格_ sycr](md0/simple.csv)
~~~

方括号内最后的几个字母：

- s/p/m/g：分别对应Simple、Pipe、Multiline、Grid 4种表格
- y/n：是否以第一行为表头
- r/l/c/d：每列的列对齐方式(r=Right 右，l=Left 左，c=Center 中，d=Default缺省)

# Fenced Div Block

Fenced Div和代码块类似，是用:::扩起来的内容，也是“活”的魔法区域，只是不是执行里面的代码。

**用md做pptx**

要写能导出pptx的markdown很简单，就如下几条规则：

1. md+pandoc只支持powerpoint缺省模板的前4个母版：标题页、节标题、标题和内容、两栏内容

1. 标题页由metadata的title、author、date、subtitle生成

1. 一级标题#生成节标题页，只有一个标题，不能有内容，否则导出的pptx会整个乱掉

1. 二级标题##根据内容生成标题和内容页或两栏内容页

    - 标题和内容页：图、表、文字(含一般文字、列表、公式等都算文字)只能有其一，内容有这3者多于1种的被分到多个页面，图/表可以有caption
    - 两栏内容页：用::::::{.columns}扩起两个:::{.column}构成两栏内容页，每栏的内容与上条的单栏内容相同。

1. 三级以上的标题作为粗体在内容中显示；图文混排可以利用caption或两栏内容，导出pptx后再做后期调整。

1. :::notes扩起来的内容在演讲提示区。

满足上述要求的md文件可以导出pptx，也可以导出pdf/docx，Fence不显示，所以可以生成能同时导出pdf/docx/pptx的md文件。

# metadata变量

除了代码块和Fenced Div Block，markdown的其他部分也可以使用pandoc插件来增强功能。

用英文百分号将metadata中的变量名扩起来，pandoc在导出时可以将它替换为变量值。这在处理某些文档时非常有用，比如合同的甲方乙方，投标书正文中经常会有很多处提及招标方和投标方的名字，使用meta变量，就可以在md正文中使用变量名，在md文档头部的metadata中定义该变量的值，pandoc导出时正文中所有变量就被替换为metadata中定义的值了，比如本文的标题为： %title% 。

注意：使用时变量(含百分号)前后不能直接连接其他文字，有加个空格。



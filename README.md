# pokemonCollection
精灵宝可梦图鉴收集

该项目使用python抓取宝可梦中文官网下的[宝可梦图鉴页面](https://cn.portal-pokemon.com/play/pokedex)，从中提取精灵数据存入mongoDB.

## 如何使用

### 安装

##### requests

[requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)是一个很实用的Python HTTP客户端库，本项目用来向宝可梦官网发起请求。

```
pip install requests
```

##### tinycss2

[tinycss2](https://pypi.org/project/tinycss2/)用来解析css样式，提供了简单易用的api。

```
pip install tinycss2
```

##### pymongo
[pymongo](https://pypi.org/project/pymongo/)，MongoDB驱动的python实现。

```
pip install pymongo
```

##### pyquery
[pyquery](https://pypi.org/project/pyquery/)是一个强大的网页解析库，提供了与jQuery相似的api，对前端开发来说很容易上手。

```
pip install pyquery
```

### 运行

##### 解析css

精灵有不同的属性类型，每种类型会显示对应的颜色值，这些颜色值存放于css文件中，pyquery解析不了css，需要使用tinycss2来解析。

命令行运行

```
python ./pokemonGo/css.py
```

结果会得到19种属性与对应颜色值，存放于mongoDB中。

因尺寸问题，截图只能显示16条数据：

![](https://raw.githubusercontent.com/kiinlam/pokemonCollection/master/images/1.png)

##### 获取列表

官网有个json请求，通过设置参数可以获取到所有精灵基础信息的列表。

命令行运行

```
python pokemon_list.py
```

##### 获取每个精灵的详情数据

通过id与子id，可以获取到对应精灵页面的html文件，然后用pyquery解析，提取出需要的数据，更新数据库中对应的条目。

命令行运行

```
python pokemon_detail.py
```

结果可得到925个精灵的数据

![](https://raw.githubusercontent.com/kiinlam/pokemonCollection/master/images/2.png)

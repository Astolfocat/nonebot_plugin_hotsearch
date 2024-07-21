<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-hotsearch

_✨ 热搜获取插件 for nonebot2 ✨_


<a href="https://cdn.jsdelivr.net/gh/TheLZY/nonebot_plugin_tuan_chatgpt@master/LICENSE.md">
    <img src="https://img.shields.io/github/license/TheLZY/nonebot_plugin_tuan_chatgpt.svg" alt="license">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>



## 📖 介绍

基于Nonebot 2.0, onebot v11的热搜获取插件~

可以获取微博、百度、知乎、贴吧、b站五个平台的最新热搜，并以合并转发的形式发送出来~

## 💿 安装


- 使用 nb-cli 安装

```
nb plugin install nonebot-plugin-hotsearch
```

- 使用 pip 安装

```
pip install nonebot-plugin-hotsearch
```

- 随后，在项目的`pyproject.toml`或`bot.py`中加上如下代码，加载插件（根据版本而定）

`pyproject.toml`中添加

```
plugins = ["nonebot_plugin_quote"]
```

或

`bot.py`中添加

```
nonebot.load_plugin("nonebot_plugin_quote")
```

## 🎉 使用

### 指令表

| 指令 | 权限 | 需要@ | 范围 |
|:-----:|:----:|:----:|:----:|
| 微博热搜 | 群员 | 否 | 群聊 |
| 百度热搜 | 群员 | 否 | 群聊 |
| 贴吧热搜 | 群员 | 否 | 群聊 |
| 知乎热搜 | 群员 | 否 | 群聊 |
| B站热搜 | 群员 | 否 | 群聊 |
> 注意: 实际触发响应需在命令前加命令前缀，具体详见`COMAND_START`配置项

## ⚙ 配置
| 配置项 | 类型 | 默认值 | 说明 |
|:------:|:----:|:-----:|:----:|
|  hotsearch_cnt| int | 10 | 热搜数量 |

## ⭐ Special thanks to

本插件在编写过程中，参考了不少以下项目，对各位大佬表示由衷的感谢，若有相关侵权问题请联系作者删除

Bot框架：
[NoneBot](https://github.com/nonebot)

README模板参考：
[A-kirami|nonebot-plugin-template](https://github.com/A-kirami/nonebot-plugin-template)

插件灵感及参考来源：
[BeiYazi0|HoshinoBot的热搜插件](https://github.com/BeiYazi0/resou)


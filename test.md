# GitHub秘籍 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
Git 和 Github 秘籍，灵感来自于 [Zach Holman](https://github.com/holman) 在 2012 年 Aloha Ruby Conference 和 2013 年 WDCNZ 上所做的演讲：[Git and GitHub Secrets](http://www.confreaks.com/videos/1229-aloharuby2012-git-and-github-secrets)([slides](https://speakerdeck.com/holman/git-and-github-secrets)) 和 [More Git and GitHub Secrets](https://vimeo.com/72955426)([slides](https://speakerdeck.com/holman/more-git-and-github-secrets))。

*其他语言版本: [English](README.md), [한국어](README.ko.md), [日本語](README.ja.md), [简体中文](README.zh-cn.md), [正體中文](README.zh-tw.md).*

# 目录
  - [GitHub](#github)
    - [不比较空白字符](#不比较空白字符)
    

## GitHub
### 不比较空白字符

在任意 diff 页面的 UR L后加上 `?w=1`，可以去掉那些只是空白字符的改动，使你能更专注于代码改动。

![Diff without whitespace](https://camo.githubusercontent.com/797184940defadec00393e6559b835358a863eeb/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031312f736563726574732f776869746573706163652e706e67)

[*详见 GitHub secrets.*](https://github.com/blog/967-github-secrets)

# `python-scripts`

> ***按需更新，脚本中给出了粗略的注释（不过这么简单估计大家一看就懂啦)***
>
> ***linux环境下可以给予脚本运行权限后放入环境变量中，便于使用***

**一些本人基于个人需要和使用习惯瞎球写成的脚本：**

1. `capacity.py`

   查看系统当前电量（仅linux可用）

   ```bash
   ❯ ./capacity.py     
   当前电量为100%
   ```

2. `checknet.py`

   测试当前网络延迟

   ```bash
   ❯ ./checknet.py            
   ██ 当前网络延迟为46.70ms.
   ```

3. `translate.py`

   基于百度翻译api的翻译脚本

   ```bash
   ❯ ./translate.py '这是一条测试' -f zh -t en
   This is a test
   ❯ trans 'this is a test' -f en -t jp         
   これはテストです
   ```

4. `automachine.py`

   用于生成自动机的状态转移图（需安装`Graphviz`）

   ```bash
   ❯ ./automachine.py
   输入接受状态：你
   请输入起点，终点，边名(空格隔开):
   我 你 爱
   ```

   ![生成示例](https://img.vim-cn.com/a1/d2c5d4008bd8dc64ea84bb598f66acd787c394.png)

5. `weather.py`

   基于和风天气api的天气脚本

   ```bash
   ❯ ./weather.py --now     
   天气状况: 多云
   温度: 2°C
   体感温度: -2°C
   风向: 西风
   风力: 2级
   降水量: 0.0毫米
   ❯ ./weather.py --forecast
   今天
       日出时间: 07:05
       日落时间: 16:16
       白天天气: 多云
       夜间天气: 晴
       最高温度: 3°C
       最低温度: -10°C
       风向: 西风
       风力: 4-5级
       降雨概率: 0%
   明天
       日出时间: 07:06
       日落时间: 16:16
       白天天气: 晴
       夜间天气: 晴
       最高温度: 0°C
       最低温度: -9°C
       风向: 南风
       风力: 1-2级
       降雨概率: 0%
   后天
       日出时间: 07:06
       日落时间: 16:16
       白天天气: 多云
       夜间天气: 多云
       最高温度: 5°C
       最低温度: -3°C
       风向: 南风
       风力: 4-5级
       降雨概率: 16%
   ```
   
6. `ipv6broadcast.py`
   
   获取东北大学ipv6直播源并写入播放列表，可供`vlc/potplayer`等播放器观看（需校园网环境运行）
   
   ```bash
   ❯ ./ipv6broadcast.py
   操作成功！已向播放列表写入188条直播数据！
   ```
   
7. `imagehost.py`

   一个简单易用的命令行图床工具，支持文件、目录上传（使用`缩狗图床api`）
   
   > 使用方法详见`./imagehost.py --help`.
   
   ```bash
   ❯ ls
   imagehost.py    pic/    pic1.jpg    pic2.jpg
   ❯ ls ./pic
   pic3.png    pic4.png
   ❯ ./imagehost.py ./pic ./pic1.jpg --type 1688
   开始上传...
   pic1.jpg : https://ae01.alicdn.com/kf/Uc199ae5fcc914575bd8dfc2e36863b1df.jpg
   pic4.jpg : https://ae01.alicdn.com/kf/U8112b51e02984363aa09337ad7748dc0g.jpg
   pic3.jpg : https://ae01.alicdn.com/kf/Uebc01361e6304815b4adabbba8a7ce51I.jpg
   上传完成，共上传3张图片!
   ```
   
8. `checkupdate.py`

   检查`qq for linux`更新的小工具，默认每五分钟刷新一次（虽然可能半年都不会更新 XD）

   ```bash
   ./checkupdate.py
   初始化完毕，以下为初始化信息：
   配置文件最后更新于2020-04-01 14:38:03
   最新版本为QQ Linux版 2.0.0 Beta2
   发布时间：2020/4/1
   ----------------------------------------
   ...(更新后在此显示)
   ```


9. `bettermark.py`

   一个十分简单的美化`chrome`导出书签的工具，需搭配[chrome-export](https://github.com/bdesham/chrome-export)使用。运行后将在当前目录生成美化后的`index.html`（虽然仍然很丑但还是比默认好了一丢丢啦）

   | 默认                                                      | 美化后                                                   |
   | --------------------------------------------------------- | -------------------------------------------------------- |
   | [demo](https://jeasonlau.xyz:10000/bookmarks/before.html) | [demo](https://jeasonlau.xyz:10000/bookmarks/index.html) |

   


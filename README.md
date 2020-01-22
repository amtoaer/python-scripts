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
   

7. `disease.py`

   > 希望大家这段时间保护好自己。

   获取[全国新型肺炎实时情况](https://3g.dxy.cn/newh5/view/pneumonia)（全国、省、自治区、直辖市、特别行政区）

   ```bash
   ❯ ./disease.py 全国  
   确诊 441 例 疑似 151 例 治愈 25 例 死亡 9 例（其中有 99 例确诊暂未明确地区 ）
   ❯ ./disease.py 湖北  
   确诊 270 例，疑似 11 例，治愈 25 例，死亡 9 例
   ❯ ./disease.py 上海 
   确诊 9 例，疑似 10 例
   ```
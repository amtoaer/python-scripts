# python-scripts
***按需更新，脚本中给出了粗略的注释（不过这么简单估计大家一看就懂啦)***

***linux环境下可以给予脚本运行权限后放入环境变量中，便于使用***

一些本人基于个人需要和使用习惯瞎球写成的脚本：

1. capacity.py：查看系统当前电量（仅linux可用）

   ```bash
   ❯ ./capacity.py     
   当前电量为100%
   ```

2. checknet.py：测试当前网络延迟

   ```bash
   ❯ ./checknet.py            
   ██ 当前网络延迟为46.70ms.
   ```

3. translate.py：基于百度翻译的翻译脚本

   ```bash
   ❯ ./translate.py '这是一条测试' -f zh -t en
   This is a test
   ❯ trans 'this is a test' -f en -t jp         
   これはテストです
   ```

4. automachine.py：用于生成自动机的状态转移图（需安装`Graphviz`)

   ```bash
   ❯ ./automachine.py
   输入接受状态：你
   请输入起点，终点，边名(空格隔开):
   我 你 爱
   ```

   ![生成示例](https://img.vim-cn.com/a1/d2c5d4008bd8dc64ea84bb598f66acd787c394.png)
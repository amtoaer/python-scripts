#!/usr/bin/python

import subprocess
import re

# 可以修改ping的次数(3)和网址(baidu.com)
test = subprocess.run('ping -c 3 baidu.com', shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = test.stdout.decode('utf-8')
toFind = 'time=(.+?) ms'
result = re.findall(toFind, output)
if len(result):
    sum = float(0)
    for x in result:
        sum = sum + float(x)
    result = sum / len(result)
# 这里可以修改延迟的判断界限和配色方案
    if result <= 50:
        print('\033[0;32;42m██\033[0m 当前网络延迟为{:.2f}ms.'.format(result))
    elif result > 50 and result <= 200:
        print('\033[0;33;43m██\033[0m 当前网络延迟为{:.2f}ms.'.format(result))
    elif result > 200:
        print('\033[0;31;41m██\033[0m 当前网络延迟为{:.2f}ms.'.format(result))
else:
    print('\033[0;37;47m██\033[0m 网络已断开.')

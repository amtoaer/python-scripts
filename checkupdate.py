#!/usr/bin/python
import re
import json
import time
import requests


def main():
    lastTime = 0
    print('初始化完毕，以下为初始化信息：')
    while (True):
        try:
            content = requests.get(
                'https://qzonestyle.gtimg.cn/qzone/qzactStatics/configSystem/data/1435/config1.js').text
            findResult = re.findall('params.+?({.+});', content)
            config = json.loads(findResult[0])
            if lastTime != config['zZConfigerUpdateTime']:
                printInfo(config)
                lastTime = config['zZConfigerUpdateTime']
            time.sleep(300)
        except:
            print('程序遇到了意料之外的错误，正在退出...\n错误信息如下：')
            raise


def printInfo(config):
    tempTime = time.localtime(config['zZConfigerUpdateTime'])
    updateTime = time.strftime("%Y-%m-%d %H:%M:%S", tempTime)
    print('配置文件最后更新于{}\n最新版本为{}\n{}'.format(updateTime,
                                            config['homepage']['version'], config['homepage']['publishTime']))
    print('----------------------------------------')


if __name__ == '__main__':
    main()

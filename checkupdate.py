#!/usr/bin/python
import re
import json
import time
import requests
import yagmail


def main():
    lastTime = getConfig()['zZConfigerUpdateTime']
    print('初始化成功，当前更新日期为：{}'.format(getTime(lastTime)))
    newTime = 0
    while True:
        try:
            newTime = getConfig()['zZConfigerUpdateTime']
            if newTime != lastTime:
                lastTime = newTime
                # 在此处依次填入你的发送邮箱，接受消息的邮箱，发送邮箱的密码，邮件服务器地址，以下为示例填写
                # 在该示例中，mail@allwens.fun会向b1361974998@gmail.com发送一封通知邮件
                mail('mail@allwens.fun', 'b1361974998@gmail.com',
                     'passwd', 'smtp.exmail.qq.com', getTime(newTime))
        except:
            print('出现了意料之外的错误，正在退出...')
            exit()
        time.sleep(300)


def getConfig():
    content = requests.get(
        'https://qzonestyle.gtimg.cn/qzone/qzactStatics/configSystem/data/1435/config1.js').text
    findResult = re.findall('params.+?({.+});', content)
    config = json.loads(findResult[0])
    return config


def getTime(stamp):
    tempTime = time.localtime(stamp)
    updateTime = time.strftime("%Y-%m-%d %H:%M:%S", tempTime)
    return updateTime


def mail(src, dst, passwd, host, updateTime):
    yag = yagmail.SMTP(user=src, password=passwd, host=host)
    text = '检测到LinuxQQ更新，更新日期为：{}'.format(updateTime)
    content = [text]
    try:
        yag.send(dst, '更新提示', contents=content)
    except:
        print(text)


if __name__ == '__main__':
    main()

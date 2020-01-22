#!/usr/bin/python
import re
import click
import requests
from bs4 import BeautifulSoup


@click.command()
@click.argument('area')
def main(area):
    # {省市:情况}字典
    dic = {}
    # 请求网页内容
    html = requests.get('https://3g.dxy.cn/newh5/view/pneumonia')
    html.encoding = 'utf=8'
    soup = BeautifulSoup(html.text, features='lxml')
    # 正则表达式
    re1 = r'全国：?\s*(.+)$'
    re2 = r'(.+?)\s+(.+)$'
    # 全国信息位于的标签与省市不同，分开处理
    country = soup.findAll('p', class_='confirmedNumber___3WrF5')[0].get_text()
    dic['全国'] = re.search(re1, country).groups()[0]
    # 遍历省市数据，使用正则表达式匹配，构建字典
    for item in soup.findAll('p', class_='descList___3iOuI'):
        content = item.get_text()
        # 使用try except忽略某些无关信息
        try:
            temp = re.search(re2, content).groups()
            dic[temp[0]] = temp[1]
        except:
            continue
    # 对输入内容进行查找
    result = False
    for item in dic.items():
        if area in item[0]:
            print(item[1])
            result = True
            break
    if not result:
        print('该地区目前无病例')


if __name__ == '__main__':
    main()

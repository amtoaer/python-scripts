#!/usr/bin/python

import requests
import re


class feed:
    def __init__(self):
        self.videolist = []
        self.count = 0
        # 播放列表的保存路径，自行修改
        self.path = '/home/jeasonlau/Videos/校内直播源.xspf'

    def findVideoUrl(self):
        html = requests.get('https://hdtv.neu6.edu.cn/index.html').text
        title_and_href = r'<td >(.+?)<br /><a href="(.+?)">'
        temp = re.findall(title_and_href, html)
        # 笨比去重大法！(保证无重复节目，但其实重复节目的播放源并不相同，可自行反注释19-29行，不进行去重)
        temp2 = []
        for item1 in temp:
            flag = True
            for item2 in temp2:
                if item1[0] == item2[0]:
                    flag = False
                    break
            if flag == True:
                temp2.append(item1)
        # for item in temp:
        for item in temp2:
            url = 'https://hdtv.neu6.edu.cn/' + item[1]
            d_html = requests.get(url).text
            find_feed = r'src="(.+?).m3u8'
            find = re.search(find_feed, d_html)
            feed_url = find.group(1) + '.m3u8'
            temp_tuple = (item[0].strip(), feed_url)
            self.videolist.append(temp_tuple)

    def writeInFile(self):
        fo = open(self.path, 'w')
        fo.write('<?xml version="1.0" encoding="UTF-8"?>\n<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\n<trackList>\n')
        for item in self.videolist:
            text = '<track>\n<title>'+item[0]+'</title>\n<location>'+item[1]+'</location>\n<extension application="http://www.videolan.org/vlc/playlist/0">\n<vlc:id>'+str(
                self.count) + '</vlc:id>\n</extension>\n</track>\n'
            fo.write(text)
            self.count = self.count+1
        fo.write('</trackList>\n</playlist>')
        fo.close()
        print('操作成功！已向播放列表写入', self.count, '条直播数据！')


if __name__ == '__main__':
    a = feed()
    a.findVideoUrl()
    a.writeInFile()

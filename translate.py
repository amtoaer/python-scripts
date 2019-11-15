#!/usr/bin/python
# coding=utf-8
import sys
import click
import http.client
import hashlib
import urllib
import random
import json
@click.command()
@click.argument('sentence')
@click.option('-f', default='auto', help='Language you want to translate.')
@click.option('-t', default='en', help='Language you want to translate to.')
# appid和密钥可以在百度翻译开放平台获取
def main(sentence, f, t):
    q = sentence
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = f  # 原文语种
    toLang = t  # 译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        dst = str(result['trans_result'][0]['dst'])
        print(dst)

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    main()

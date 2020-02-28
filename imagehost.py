#!/usr/bin/python

import requests
import click
import os

# 这里列举了几种常见的图片格式，其它格式可以修改后自行测试
allowedExtension = ['.jpeg', '.bmp', '.jpg', '.png', '.webp']
url = ''


@click.command()
@click.option('--type', '-t', default='1688', type=click.Choice(['1688', 'tieba', '360', 'taobao', 'smms', 'sohu', 'jd']), help='image hosting service.')
@click.argument('paths', nargs=-1, type=click.Path(exists=True, readable=True))
def main(type, paths):
    global url
    url = 'https://pic.suo.dog/api/tc.php?type={}&echo=imgurl'.format(type)
    count = 0
    print('\033[33m开始上传...\033[0m')
    for path in paths:
        if os.path.isdir(path):
            if not path.endswith('/'):
                path += '/'
            items = os.listdir(path)
            for item in items:
                if os.path.isfile(path + item):
                    count += uploadFile(path + item)
        else:
            count += uploadFile(path)
    print('\033[33m上传完成，共上传{}张图片!\033[0m'.format(count))


def uploadFile(file):
    if os.path.splitext(file)[-1] in allowedExtension:
        postContent = {'file': open(file, 'rb')}
        with requests.post(url, files=postContent) as response:
            print('\033[31m{}\033[0m : \033[4;32m{}\033[0m'.format(
                os.path.basename(file), response.text))
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()

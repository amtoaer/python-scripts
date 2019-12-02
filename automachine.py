#!/usr/bin/python

# 生成的图片自动命名为automachine_num.png，num为1...n

import os
import re


def findcount(path):
    strin = ''
    a = os.listdir(path)
    for item in a:
        strin = strin+item
        toFind = r'automachine_(\d+)'
        t = re.findall(toFind, strin)
        temp = [int(i) for i in t]
    try:
        count = max(temp) + 1
    except:
        count = 1
    finally:
        return count
# 获取当前编号


def main(count, path):
    File = open(path+'temp', 'w')
    File.write(
        """digraph finite_state_machine {
            rankdir=LR;
            size="8,5"
        """
    )
    t = str(input('输入接受状态：'))
    t = '    node [shape = doublecircle]; ' + t + ';'+'node [shape = circle];'
    File.writelines(t)
    print('请输入起点，终点，边名(空格隔开):')
    while True:
        try:
            a, b, c = input().split(' ')
            t = '    {起点} -> {终点} [ label= "{边名}" ];'.format(
                **{'起点': a, '终点': b, '边名': c})
            File.writelines(t)
        except:
            break
    File.writelines('}')
    File.close()
    os.system('dot -Tpng '+path+'temp >'+path+'automachine_'+str(count)+'.png')
    os.system('rm '+path+'temp')
# 新建的文件编号为当前编号+1


if __name__ == '__main__':
    # 可以手动修改保存路径
    path = '/home/admin/Pictures/automachine/'
    count = findcount(path)
    main(count, path)

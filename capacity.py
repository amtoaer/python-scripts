#!/usr/bin/python
file_object = open('/sys/class/power_supply/BAT0/capacity')
power = file_object.read().splitlines()
text = '当前电量为'+power[0]+'%'
print(text)
file_object.close()

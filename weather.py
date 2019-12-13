#!/usr/bin/python
# coding=utf-8
import requests
import click


@click.command()
@click.option('--now', 'weathertype', flag_value='now', default=True, help='show current weather.')
@click.option('--forecast', 'weathertype', flag_value='forecast', help='show weather in three days.')
def main(weathertype):
    weathertype = weathertype
    # key可前往https://www.heweather.com/注册账号后获取
    key = ''
    # 你的位置
    location = 'hunnan,shenyang'
    url = 'https://free-api.heweather.net/s6/weather/' + \
        weathertype + '?' + 'location=' + location + '&key=' + key
    r = requests.get(url)
    info = r.json()
    if weathertype == 'now':
        printnow(info)
    elif weathertype == 'forecast':
        printforecast(info)


def printnow(info):
    weatherstatus = info['HeWeather6'][0]['now']['cond_txt']
    temperature = info['HeWeather6'][0]['now']['tmp']
    feeltemperature = info['HeWeather6'][0]['now']['fl']
    winddirection = info['HeWeather6'][0]['now']['wind_dir']
    windpower = info['HeWeather6'][0]['now']['wind_sc']
    precipitation = info['HeWeather6'][0]['now']['pcpn']
    print('天气状况:', weatherstatus)
    print('温度:', temperature+'°C')
    print('体感温度:', feeltemperature+'°C')
    print('风向:', winddirection)
    print('风力:', windpower+'级')
    print('降水量:', precipitation+'毫米', end='')


def printforecast(info):
    dict = {0: '今天', 1: '明天', 2: '后天'}
    for i in range(3):
        dayweather = info['HeWeather6'][0]['daily_forecast'][i]['cond_txt_d']
        nightweather = info['HeWeather6'][0]['daily_forecast'][i]['cond_txt_n']
        sunrise = info['HeWeather6'][0]['daily_forecast'][i]['sr']
        sunset = info['HeWeather6'][0]['daily_forecast'][i]['ss']
        temperature_max = info['HeWeather6'][0]['daily_forecast'][i]['tmp_max']
        temperature_min = info['HeWeather6'][0]['daily_forecast'][i]['tmp_min']
        winddirection = info['HeWeather6'][0]['daily_forecast'][i]['wind_dir']
        windpower = info['HeWeather6'][0]['daily_forecast'][i]['wind_sc']
        rainfall = info['HeWeather6'][0]['daily_forecast'][i]['pop']
        print(dict[i])
        print('    日出时间:', sunrise)
        print('    日落时间:', sunset)
        print('    白天天气:', dayweather)
        print('    夜间天气:', nightweather)
        print('    最高温度:', temperature_max+'°C')
        print('    最低温度:', temperature_min+'°C')
        print('    风向:', winddirection)
        print('    风力:', windpower+'级')
        if i != 2:
            print('    降雨概率:', rainfall + '%')
        else:
            print('    降雨概率:', rainfall + '%', end='')


if __name__ == '__main__':
    main()

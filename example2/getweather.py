# -*- coding: utf-8 -*-

# http://toy.weather.com.cn/SearchBox/searchBox?_=1362892474803&language=zh&keyword=%E5%8C%97%E4%BA%AC

from __future__ import print_function
import sys
sys.path.insert(0, "../")

import json
import pandas as pd
from aiml.constants import *
if PY3:
    import urllib.request
else:
    import urllib

ENCODING = 'utf-8'

df = pd.read_csv('cities.csv', sep='\t')
cncity = dict(zip(df['city'], df['ID']))
encity = dict(zip(df['english'], df['ID']))

def queryLocation(term):
    if term in cncity:
        return cncity[term]
    if term in encity:
        return encity[term]
    print("找不到地点")
    return

def queryRealTimeWeatherInfo(code):
    #url = "http://m.weather.com.cn/data/%s.html" % code
    url = "https://api.seniverse.com/v3/weather/now.json?key=zkffhieb2wd92rwt&location=%s&language=zh-Hans&unit=c" % code
    resp = urllib.request.urlopen(url) if PY3 else urllib.urlopen(url)
    data = json.load(resp)
    if not data:
        print("找不到天气预报")
    data = data['results'][0]
    info = {}
    info['name'] = data['location']['name']
    info['last_update'] = data['last_update']
    for k, v in data['now'].items():
        info[k] = v
    return info

def showRealTimeWeatherInfo(info):
    # template = u"{city} {time} 天气实况: 气温{temp}℃, {WD}{WS}, 湿度{SD}"
    template = u"{name}, {last_update}, 天气实况: 气温{temperature}℃, {text}"
    # template = u"{name} {last_update} 天气实况: 气温{temperature}℃, {text}"
    # print(template.format(**info))
    response = template.format(**info).encode(ENCODING)
    if PY3:
        response = response.encode(ENCODING) if type(response) == str else response.decode('utf-8')
    print(response)


def main():
    assert len(sys.argv) >= 3
    function = sys.argv[1]
    term = ''.join(sys.argv[2:])
    if function == 'realtime':
        # 实时
        location = queryLocation(term)
        if location:
            showRealTimeWeatherInfo(queryRealTimeWeatherInfo(location))

if __name__ == '__main__':
    main()

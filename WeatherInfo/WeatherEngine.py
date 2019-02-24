# -*- coding: utf-8 -*-

import sys     
import requests

class queryWeatherEngine( object):
    def __init__(self):
        print('queryWeatherEngine constructor')
             

    def queryWeather(self,cityName):
        print('* queryWeather  ')        
        cityCode = self.transCityName(cityName)

        rep = requests.get('http://www.weather.com.cn/data/sk/' + cityCode + '.html')
        rep.encoding = 'utf-8'
        print( rep.json() ) 
        
        msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
        msg2 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
        msg3 = '温度: %s' % rep.json()['weatherinfo']['temp'] + ' 度' + '\n'
        msg4 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n'
        msg5 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5
        return result
        
    def transCityName(self ,cityName):
        cityCode = ''
        if cityName == '北京' :
            cityCode = '101010100'
        elif cityName == '天津' :
            cityCode = '101030100'
        elif cityName == '上海' :
            cityCode = '101020100'
            
        return cityCode
                
        
if __name__=="__main__":  
    print("aa")
    server = queryWeatherEngine()
    ret = server.queryWeather("北京")
    print(ret)

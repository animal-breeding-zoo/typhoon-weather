#!/usr/bin/env python
import requests
import configparser

conf = configparser.ConfigParser()
conf.read("env/resource.ini")
KEY = conf.get('httpclient', 'key')
WEATHER_URL = conf.get('httpclient', 'weather_url')
PM25_URL = conf.get('httpclient', 'pm25_url')

class QCodeService:
    def requestPM25(self, city):
        params={'key':KEY,'city':city}
        req = requests.get(PM25_URL, params=params)
        if req.status_code == 200:
            return req.json()['result'][0]
        return None

    def requestWeather(self, city):
        params={'key':KEY,'city':city}
        req = requests.get(WEATHER_URL, params=params)
        if req.status_code == 200:
            return req.json()['result'][0]
        return None


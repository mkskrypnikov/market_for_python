#!/usr/bin/env python
# coding: utf-8

print('импорот пакетов')
import pandas as pd
import json
import requests
from requests.exceptions import ConnectionError
from time import sleep
import json
from datetime import datetime as dt
from datetime import date, timedelta
import time
import datetime
import numpy as np
from urllib.request import Request, urlopen
from pandas.io.json import json_normalize
import contextlib
import os
import csv
import calendar


print('формирование дат')
lastday = datetime.datetime.now()
lastday = lastday - timedelta(days=1)
lastday0 =  lastday.strftime("%d-%m-%Y")
lastdayx = lastday.strftime("%Y-%m-%d")

lastday1 = datetime.datetime.now()
lastday1 = lastday1 - timedelta(days=2) 
lastday10 = lastday1.strftime("%d-%m-%Y")
lastday11 = lastday1.strftime("%Y-%m-%d")

lastday2 = datetime.datetime.now()
lastday2 = lastday2 - timedelta(days=3) 
lastday20 = lastday2.strftime("%d-%m-%Y")
lastday22 = lastday2.strftime("%Y-%m-%d")



start_dates = lastday20
end_dates = lastday0
start_datesg = lastday22
end_datesg = lastdayx

'''''
start_datesg = '2020-02-01'
end_datesg = '2020-02-13'
start_dates = '01-02-2020'
end_dates = '13-02-2020'
'''''

start_date = dt.strptime(start_dates, '%d-%m-%Y')
end_date = dt.strptime(end_dates, '%d-%m-%Y')

print('данные для отчета')
at = 'xxx'
cid = 'xxx'
mag = [xxx, xxx, xxx, xxx]
magname = ['xxx', 'xxx', 'xxx', 'xxx']




start_time = dt.now()
print('формирование отчета')
print(mag)
print(start_date)
print(end_date)

datdat = [lastday0, lastday10, lastday20]
datdatday = [lastdayx, lastday11, lastday22]

parmag = 0
info_offer = pd.DataFrame()
info_offer_itog = pd.DataFrame()
while parmag <= 3:
    pardat = 0
    while pardat <=2:
        y= 999
        i=1
        while y >= 999:
            url = 'https://api.partner.market.yandex.ru/v2/campaigns/'+str(mag[parmag])+'/stats/offers.json?fromDate='+str(datdat[pardat])+'&toDate='+str(datdat[pardat])+'&fields=url&pageSize=999'+'&page='+str(i)+'&oauth_token='+at+'&oauth_client_id='+cid
            print(datdat[pardat])
            print(magname[parmag])
            print(i)
            info_offer = []
            response = urlopen(url)
            elevations = response.read()
            data = json.loads(elevations)
            info_offer_offer = json_normalize(data['offersStats'])
            info_offer = json_normalize(data['offersStats'], record_path ='offerStats')
            info_offer['магазин'] = magname[parmag]
            info_offer['дата'] = datdatday[pardat]
            info_offer_itog = info_offer_itog.append(info_offer, ignore_index = False)
            y = len(info_offer)
            i = i+1
        pardat = pardat+1
    parmag = parmag+1
info_offer_itog['url'] = info_offer_itog['url'].replace(to_replace ='https://www.citilink.ru/catalog/', value ='', regex =True)
info_offer_itog['url']= info_offer_itog['url'].str.split("?", n = 1, expand = True)
info_offer_itog['категория'] = info_offer_itog['url'].str.rsplit('/', n = 3, expand = True)[1]
info_offer_itog['cost'] = info_offer_itog['spending'].astype(float)*30
info_offer_itog.to_csv('market_cost_offer_t.csv', index=False, header=True, sep=';', encoding='cp1251')
print(dt.now() - start_time)
info_offer_itog.head()




start_time = dt.now()
print('актуализация данных очтета')
x1 = pd.read_csv('market_cost_offer_t.csv', sep=';', encoding='cp1251', header=0)
x2 = pd.read_csv('market_cost_offer.csv', sep=';', encoding='cp1251', header=0)

x2 = x2[x2.дата.str.contains(lastdayx)==False]
x2 = x2[x2.дата.str.contains(lastday11)==False]
x2 = x2[x2.дата.str.contains(lastday22)==False]


x2 = x2.append(x1, ignore_index=False)
x2.to_csv('market_cost_offer.csv', index=False, header=True, sep=';', encoding='cp1251')
print(dt.now() - start_time)









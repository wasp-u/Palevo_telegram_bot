from urllib.request import urlopen
import json
import requests

import logging
import client
logger = logging.getLogger('uz.client')
# logger.debug('Headers: %s', kwargs['headers'])
# logger.debug('Cookies: %s', self.session.cookies)


def getStation():
    station_1 = urlopen('http://booking.uz.gov.ua/en/purchase/station/?term=Kyiv').read().decode('utf-8')
    station_2 = urlopen('http://booking.uz.gov.ua/en/purchase/station/?term=Kramatorsk').read().decode('utf-8')

    print(station_1)
    print(station_2)


    station_1Json = json.loads(station_1)
    station_2Json = json.loads(station_2)

    return station_1Json[0]['value'],station_2Json[0]['value']

def get_staton_by_name(station):
    st = urlopen('http://booking.uz.gov.ua/en/purchase/station/?term='+station).read().decode('utf-8')
    print(st)
    station_1 = json.loads(st)

    rezult = []
    for i in station_1:
        rezult.append((i['title'],i['value']))
    return rezult

def checkTrains(id_1,id_2):
    # http: // booking.uz.gov.ua / en / purchase / search /
    params = {
    'station_id_from': id_1,  # ID станции отправления
    'station_id_till': id_2, # ID станции назначения
    'date_dep': '09.30.2017',     # дата отправления в формате mm.dd.yyyy
    'time_dep': '00:00',
    'time_dep_till':'',
    'another_ec':0,
    'search':''
    }
    r = requests.post('http://booking.uz.gov.ua/en/purchase/search/',data=params).json()

    print('----',r['value'][0])
    return r


def shawTrain(id_1,id_2,date):

    # t = requests.head()
    params = {
        'station_id_from': id_1,  # ID станции отправления
        'station_id_till': id_2,  # ID станции назначения
        'date_dep': 1506741720,
        'train': '712K',# номер поезда
        'model': 1, # модель поезда
    'coach_type': 'C2', # тип вагона (люкс, купе, и т. д.)
    'round_trip': 0,
    'another_ec': 0
    }
    r = requests.post('http://booking.uz.gov.ua/en/purchase/coaches/',data=params)



    # station_1 = urlopenn('http://booking.uz.gov.ua/en/purchase/coaches/?'
    #                     'station_id_from = 2200001 &'
    #                     ' station_id_till = 2214110 & train = 712 % D0 % 9A & '
    #                     'coach_type = % D0 % A11 & '
    #                     'date_dep = 1506741720 & round_trip = 0 & another_ec = 0').read().decode('utf-8')
    #
    print(r.text)
    # print(station_1)

if __name__=="__main__":
    print(getStation())
    id_1,id_2 = getStation()
    checkTrains(id_1,id_2)
    shawTrain(id_1,id_2,1506741720)

    # c=client.UZClient()
    # t=c.list_trains('10.10.2017',2200001,2214110)
    # for i in t:
    #     print(i)


#!/usr/bin/python
# coding: utf-8

import traceback
import sys
import csv
sys.path.append("/usr/lib/python3.9/site-packages/MyPyDHT-0.1-py3.9-linux-armv7l.egg")
import MyPyDHT

csv_output = '/home/takehiko/work/csv/room_temp.csv'


def get_room_temparature():

    try:
        humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 26)
        return [temperature, humidity]
    except BaseException as e:
        traceback.print_exc()
        get_room_temparature()  # リトライする


with open(csv_output, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(get_room_temparature())


#!/usr/bin/python
# coding: utf-8

############################################## 
# センサー制御取得 - ここから
# 
import sys
sys.path.append("/usr/lib/python3.9/site-packages/MyPyDHT-0.1-py3.9-linux-armv7l.egg")

import MyPyDHT

# 測定の開始(26は、接続したGPIOポート)
humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 26)

# 結果の表示
print("Temp=" + str(temperature) + "*C, Humidity = " + str(humidity) + "%")

# 
# センサー制御取得 - ここまで
##############################################


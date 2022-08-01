import socket
import time
import sys
sys.path.append("/usr/lib/python3.9/site-packages/MyPyDHT-0.1-py3.9-linux-armv7l.egg")
import MyPyDHT
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# タイムアウトの設定は必要か
server.settimeout(0.2)


# 測定の開始(26は、接続したGPIOポート)
humidity, temperature = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, 26)
time_now = str(datetime.datetime.now())
message = "Temp=" + str(temperature) + "*C, Humidity = " + str(humidity) + "%, time=" + time_now



for count in range(3):
    server.sendto(message.encode(), ('<broadcast>', 37020))
    print("message sent!")
    time.sleep(1)

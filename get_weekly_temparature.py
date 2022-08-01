import json
import requests
import csv
import datetime
import pytz


csv_output = '/home/takehiko/work/csv/weekly_temp.csv'



class temperature_data:
    
    def __init__(self, mesuretime, temperature_api, humidity_api):
        self.mesuretime = mesuretime
        self.temperature_api = temperature_api
        self.humidity_api = humidity_api


def get_openmeteo_hourly():
    tz = pytz.timezone("Asia/Tokyo")
    standard_date = datetime.datetime.now()
    cleaned_date = standard_date.replace(minute=0, second=0, microsecond=0)
    start_date = tz.localize(cleaned_date).strftime('%Y-%m-%d')
    end_date = tz.localize(cleaned_date + datetime.timedelta(days=8)).strftime('%Y-%m-%d')

    # requestsのために辞書型を使うと","や"%2F"が勝手に変換されてしまうためうまく呼び出せず。文字列としてURLを指定
    url = "https://api.open-meteo.com/v1/forecast?"
    payload_str = "latitude=35.6785&longitude=139.6823&"
    payload_str = payload_str + "hourly=temperature_2m,relativehumidity_2m&"
    payload_str = payload_str + "timezone=Asia%2FTokyo&"
    payload_str = payload_str + "start_date=" + start_date + "&"
    payload_str = payload_str + "end_date=" + end_date

    response = requests.get(url + payload_str)
    return response.text


hourly_return = get_openmeteo_hourly()
data = json.loads(hourly_return)

with open(csv_output, 'w') as f:
    writer = csv.writer(f)
    for count in range(len(data['hourly']['time'])):
        time = data['hourly']['time'][count]
        temperature = data['hourly']['temperature_2m'][count]
        humidity = data['hourly']['relativehumidity_2m'][count]
        writer.writerow([time, temperature, humidity, "", ""])


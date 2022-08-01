import psycopg2
import datetime
import pytz
import csv

csv_output = '/home/takehiko/work/csv/room_temp.csv'


def iso_to_jstformat():
    dt = None
    try:
        tz = pytz.timezone("Asia/Tokyo")
        dt = datetime.datetime.now()
        dt_true = dt.replace(minute=0, second=0, microsecond=0)
        d = tz.localize(dt_true)
        return d.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            tz = pytz.timezone("Asia/Tokyo")
            dt = datetime.datetime.now()
            dt_true = dt.replace(minute=0, second=0, microsecond=0)
            d = tz.localize(dt_true)
            return d.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            pass
    return dt


def get_room_temp():
    with open(csv_output, 'r') as r:
        csvreader = csv.reader(r)
        for row in csvreader:
            return row
        

# パスワードは$PGPASSWORDに保管。非推奨のため~/.pgconnに切り替えをいつかしたい
conn = psycopg2.connect(database='temperature', user='temperature')
cursor = conn.cursor()

room_data = get_room_temp()

_sql = 'update temp_info SET temperature_sensor = '
_sql = _sql + room_data[0] + ', humidity_sensor = '
_sql = _sql + room_data[1] + ' WHERE get_time = \''
_sql = _sql + iso_to_jstformat() + '\';'

cursor.execute(_sql)
conn.commit()
cursor.close()
conn.close()


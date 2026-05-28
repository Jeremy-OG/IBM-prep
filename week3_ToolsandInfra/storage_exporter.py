from prometheus_client import start_http_server, Gauge
import time
import json

TEMPERTATURE = Gauge('storage_temperature_celsius', 'Drive temperature')
READS_PER_SEC = Gauge('storage_reads_per_sec', 'Disk reads per second')
WRITES_PER_SEC = Gauge('storage_writes_per_sec', 'Disk writes per second')
SMART_STATUS = Gauge('storage_smart_status','Drivehealth status 1=healthy 0=unhealthy')


if __name__ == '__main__':
    start_http_server(8000)
    while True:
        with open('smart_sample.json','r') as file:
            data = json.loads(file)
            temp = data['temperature']["current"]
            status = data['smart_status']['passed']


from prometheus_client import start_http_server, Gauge
import time
import json
from week1_StorageConcepts.disk_stats import read_diskstats

TEMPERTATURE = Gauge('storage_temperature_celsius', 'Drive temperature')
READS_PER_SEC = Gauge('storage_reads_per_sec', 'Disk reads per second')
WRITES_PER_SEC = Gauge('storage_writes_per_sec', 'Disk writes per second')
SMART_STATUS = Gauge('storage_smart_status','Drive health status 1=healthy 0=unhealthy')


if __name__ == '__main__':
    start_http_server(8000)
    while True:
        with open('week2_PyDepth/smart_sample.json','r') as file:
            data = json.load(file)
            temp = data['temperature']["current"]
            status = data['smart_status']['passed']
        TEMPERTATURE.set(temp)
        SMART_STATUS.set(1 if status else 0)
        prev = read_diskstats()
        time.sleep(15)
        curr = read_diskstats()

        for device in curr:
            if device =="sdd":
                reads_sec = (curr[device][0] - prev[device][0]) / 15
                writes_sec = (curr[device][1] - prev[device][1]) / 15
                READS_PER_SEC.set(reads_sec)
                WRITES_PER_SEC.set(writes_sec)

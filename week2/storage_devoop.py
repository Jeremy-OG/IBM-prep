from dataclasses import dataclass
import json

@dataclass
class DiskHealth:
    temperature: int
    power_on_hours:int
    reallocated_sectors: int
    healthy: bool



class StorageDevice:
    def __init__(self,devPath):
        self.devPath = devPath

    @property
    def capacity(self):
       with open(f'/sys/block/{self.devPath}/size','r') as f:
           for line in f:
               byte_sectors = line
               GB = int(byte_sectors)/1e9
               return round(GB,5)
    @property
    def is_ssd(self):
        with open(f"/sys/block/{self.devPath}/queue/rotational", 'r') as f:
            for line in f:

                if int(line) == 1:
                    return False
                else:
                    return True

    @property
    def name(self):
        with open(f"/sys/block/{self.devPath}/device/model",'r') as f:
            for line in f:
                return line.strip()
            
    def get_smart_health(self):
        with open(self.devPath,"r") as f:
            data = json.load(f)

        return DiskHealth(
            temperature=data["temperature"]["current"],
            power_on_hours=data["power_on_time"]["hours"],
            reallocated_sectors=data["ata_smart_attributes"]["table"][0]["raw"]["value"],
            healthy=data['smart_status']['passed']
        )
        

path = StorageDevice('smart_sample.json')

print(path.get_smart_health())
#print(f"Capacity: {path.capacity} GB")
#print('--------------')
#print(f"Path is ssd: {path.is_ssd}")
#print('--------------')
#print(f"Model: {path.name}")


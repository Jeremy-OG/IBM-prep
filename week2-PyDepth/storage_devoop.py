from dataclasses import dataclass
import json
from typing import Optional
import asyncio
import aiofiles


@dataclass
class DiskHealth:
    temperature: int
    power_on_hours:int
    reallocated_sectors: int
    healthy: bool



class StorageDevice:
    def __init__(self,devPath:str) -> None:
        self.devPath = devPath

    @property
    def capacity(self) -> float:
       with open(f'/sys/block/{self.devPath}/size','r') as f:
            byte_sectors = f.read().strip()
            GB = int(byte_sectors)/1e9
            return round(GB,5)
    @property
    def is_ssd(self) -> bool:
        with open(f"/sys/block/{self.devPath}/queue/rotational", 'r') as f:
            return f.read().strip() == 0

    @property
    def name(self) -> Optional[str]:
        with open(f"/sys/block/{self.devPath}/device/model",'r') as f:
                return f.read().strip() or None
            
    async def get_smart_health(self) -> DiskHealth:
        async with aiofiles.open(self.devPath,'r') as f:
            content = await f.read()
            py_string = json.loads(content)


            return DiskHealth(
                temperature=py_string["temperature"]["current"],
                power_on_hours=py_string["power_on_time"]["hours"],
                reallocated_sectors=py_string["ata_smart_attributes"]["table"][0]["raw"]["value"],
                healthy=py_string['smart_status']['passed']
        )
        

path = StorageDevice('smart_sample.json')

result = asyncio.run(path.get_smart_health())
print(result)



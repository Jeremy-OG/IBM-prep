import requests
from dataclasses import dataclass
from typing import Optional

@dataclass
class DriveHealth:
    name:str
    state:str    #"Enabled", "Disabled"
    health:str    # "OK", "Warning", "Critical"
    capacity_bytes:int    
    protocol:str     #"NVMe", "SAS", "SATA"

class RedfishClient:

    def __init__(self,base_url:str,user:str,password:str):
        self.base_url = base_url
        self.user = user
        self.password = password

    def get(self,path:str)->dict:
        pass

    def get_drives(self)->list[DriveHealth]:
        pass
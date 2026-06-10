import requests
from dataclasses import dataclass
from typing import Optional
import json

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
        response = requests.get(self.base_url+path,
                    auth=(self.user,self.password),
                    verify=False)
        return response.json()

    def get_drives(self)->list[DriveHealth]:
        systems=self.get("/redfish/v1/Systems")
        drives=[]
        for system in systems["Members"]:
            storage = self.get(system["@odata.id"]+"/Storage")
            for controller in storage["Members"]:
                drive_collection=self.get(controller["@odata.id"]+"/Drives")
                for drive_ref in drive_collection["Members"]:
                    drive = self.get(drive_ref["@odata.id"])
                    drives.append(DriveHealth(
                        name=drive["Name"],
                        state=drive["Status"]["State"],
                        health=drive["Status"]["Health"],
                        capacity_bytes=drive["CapacityBytes"],
                        protocol=drive["Protocol"]
                    ))

        return drives
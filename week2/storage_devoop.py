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

path = StorageDevice('sda')

print(f"Capacity: {path.capacity} GB")
print('--------------')
print(f"Path is ssd: {path.is_ssd}")
print('--------------')
print(f"Model: {path.name}")
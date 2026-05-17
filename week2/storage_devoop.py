class StorageDevice:
    def __init__(self,devPath):
        self.devPath = devPath

    def get_capacity(self):
       with open(f'/sys/block/{self.devPath}/size','r') as f:
           for line in f:
               byte_sectors = line
               bytes = int(byte_sectors) *512
               GB = int(byte_sectors)/1e9
               print("bytesectors:", byte_sectors)
               print('bytes:', bytes )
               print("GigaBytes", GB)
    
    
    def is_ssd(self):
        pass

    def get_name(self):
        pass

path = StorageDevice('sda')

path.get_capacity()
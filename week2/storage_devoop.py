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
        with open(f"/sys/block/{self.devPath}/queue/rotational", 'r') as f:
            for line in f:

                if int(line) == 1:
                    print("FALSE, it is HDD")
                else:
                    print("TRUE, it is SSD")

    def get_name(self):
        pass

path = StorageDevice('sda')

path.get_capacity()
print('--------------')
path.is_ssd()

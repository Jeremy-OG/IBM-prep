class StorageDevice:
    def __init__(self,devPath):
        self.devPath = devPath

    def get_capacity(self):
        pass
    
    def is_ssd(self):
        pass

    def get_name(self):
        pass

path = StorageDevice('/sys/block')



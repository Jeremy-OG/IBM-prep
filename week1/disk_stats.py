import time

def read_diskstats():
    stats ={}
    with open("/proc/diskstats",'r') as f:
        for line in f:
            parts = line.split()
            device = parts[2] # device type
            reads = int(parts[3]) # total reads done 
            writes = int(parts[7]) # total reads done
            stats[device] = (reads,writes)
    return stats
prev = read_diskstats()

while True:
    time.sleep(2)
    print(f"{"DEVICE":<12}{"READS/S":<12}{"WRITES/S":<12}")
    print("-"*36)
    curr = read_diskstats()
    for device in curr:
        reads_sec = (curr[device][0] -prev[device][0])/2
        writes_sec = (curr[device][1]-prev[device][1])/2
        print(f"{device:<12}{reads_sec:<12.1f}{writes_sec:<12}")
    prev = curr


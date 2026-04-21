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
print(prev)
print(f"{"DEVICE":<20}{"FS_TYPE":<12}{"OPTIONS"}")
print("-----------         --------    --------")
with open("/proc/mounts","r") as f:
    for line in f:
        parts = line.split()
        device = parts[0]
        fs_type = parts[2]
        options = parts[3]
        print(f"{device:<20}{fs_type:<12}{options}")




import json
with open("RepNVMe.json","r") as nvm: # or actual file path to NVMe metrics
    nvm_data = json.load(nvm)
print(f"{"NVMe Health Summary":<20}")
print(f"{"-----------------":<20}")
for key,value in nvm_data.items():
    if isinstance(value,list):
        active = [v for v in value if v!=0]
        print(f"{key:<20}:{active}")
    else:
        print(f"{key:<20}:{value}")

## Parity simulation Practice/ XOR practice
def Simulations(x):
    total = 0
    for i in x:
        total^= i

    return total

print(Simulations([10,20,45]))


## Nice Simulation of failed Drive and recovered data in RAID 5 setup
def new_sim(y,failed_index,parity):
    new_total = 0
    for i in range(len(y)):
        if i!=failed_index:
            new_total^=y[i]
    new_total^=parity

    return new_total


## Simulation of finding data, comparing it to 
parity = 51
new_drives = [10,0,45]
failed_index = 1

recovered = new_sim(new_drives, failed_index, parity)

if recovered :
    print(f"Recovery successful! Drive {failed_index} value {recovered} recovered correctly.")
else:
    print(f"Recovery failed.")

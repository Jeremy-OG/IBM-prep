def Simulations(x):
    total = 0
    for i in x:
        total^= i

    return total

#print(Simulations([10,20,45]))
parity = Simulations([10,20,45])

def new_sim(y,failed_index,parity):
    new_total = 0
    for i in range(len(y)):
        if i!=failed_index:
            new_total^=y[i]
    new_total^=parity

    return new_total

print(new_sim([10,20,45],1,51))

drives = [10, 20, 45]
failed_index = 1
parity = Simulations(drives)
recovered = new_sim(drives, failed_index, parity)

if recovered == drives[failed_index]:
    print(f"Recovery successful! Drive {failed_index} value {recovered} recovered correctly.")
else:
    print(f"Recovery failed.")
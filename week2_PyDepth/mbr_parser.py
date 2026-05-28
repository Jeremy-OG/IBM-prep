import struct

PARTITION_OFFSET = 446
ENTRY_SIZE = 16
NUM_PARTITIONS = 4

def parse_mbr(file_path):
    with open(file_path,"rb") as f:
        f.seek(PARTITION_OFFSET)
        f.seek(510)
        sig = f.read(2)
        print(f"MBR Signature: {hex(sig[0])} {hex(sig[1])}")
        f.seek(PARTITION_OFFSET)

        for i in range(NUM_PARTITIONS):
            entry = f.read(ENTRY_SIZE)
            
            status, part_type, lba_start, sector_count = struct.unpack('<BxxxBxxxII',entry)


            print(f'Partition {i + 1}')
            print(f" Status     :{'Bootable' if status ==  0x80 else 'Not Bootable'}")
            print(f" Type       :{hex(part_type)} ")
            print(f" LBA Start  : {lba_start}")
            print(f" Sector Count : {sector_count}")
            print(f" Size (MB)    : {round(sector_count * 512 / 1e6, 2)}")
            print()

parse_mbr("mbr_test.bin")

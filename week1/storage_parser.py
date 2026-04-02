# Must install sg3-utils on linux to read hardware and run program
#Run sudo sg_inq /dev/sda to see the info you will need to parse
import subprocess

result = subprocess.run(
    ["sudo","sg_inq", "/dev/sda"],
    capture_output=True,
    text=True
)

print(result.stdout)
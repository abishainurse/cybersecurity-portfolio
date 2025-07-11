import subprocess
import sys

def ping(IP):
    result = subprocess.run(["ping", "-n", "1", IP])

    return result.returncode == 0

def Scan(file):

    try:
        with open(file, "r") as file:
            IPLIST = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    for i in range(len(IPLIST)):
        IPLIST[i] = IPLIST[i].strip()

    for IP in IPLIST:
        if ping(IP):
            print(f"{IP}: Host can be pinged")
        else:
            print(f"{IP}: Host can't be pinged")


if __name__ == "__main__":
    file = sys.argv[1]
    Scan(file)

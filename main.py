import os 
import time
import fetch_PID

import pyuac
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()

pids = fetch_PID.fetch()
print(pids)
count = 0
for pid in pids:
    try:
        os.system("procdump.exe "+str(pid))
        count += 1
    except:
        print("cannot create dump for system processes")
print(count)
time.sleep(10)
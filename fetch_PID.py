import psutil

system_processes = ["System","System Idle Process","explorer.exe","ntoskrnl.exe","WerFault.exe","backgroundTaskHost.exe","backgroundTransferHost.exe","winlogon.exe","wininit.exe","csrss.exe","lsass.exe","smss.exe","services.exe","taskeng.exe","taskhost.exe","dwm.exe","conhost.exe","svchost.exe","sihost.exe"]
def fetch():
    pids = []
    for process in psutil.process_iter(["pid","name"]):
        if process.info["name"] not in system_processes:
            pids.append(process.info["pid"])
            print(process)
    return pids

#!python3

import os
import time
import ctypes
import psutil
import cpuinfo
import getpass
import platform
from termcolor import colored
from colorama import init; init()

# Uptime Credits to: AlexFlipnote's neofetch-win
def uptime():
        """ Get the device uptime """
        delta = round(time.time() - psutil.boot_time())

        hours, remainder = divmod(int(delta), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        def includeS(text: str, num: int):
            return f"{num} {text}{'' if num == 1 else 's'}"

        d = includeS("day", days)
        h = includeS("hour", hours)
        m = includeS("minute", minutes)
        s = includeS("second", seconds)

        if days:
            output = f"{d}, {h}, {m} and {s}"
        elif hours:
            output = f"{h}, {m} and {s}"
        elif minutes:
            output = f"{m} and {s}"
        else:
            output = s

        return output


cpu_info = (cpuinfo.get_cpu_info()) # Tuple

# Computer & Username + Underscor
username = getpass.getuser()
computername = platform.node()
fullname = username + "@" + computername
underscore_list = []
underscore_list.append(len(fullname) * "-")

hostcmd = "wmic csproduct get name"
hostcmd = os.popen(hostcmd).read().split()
hostcmd.remove('Name')

kcmd = "wmic os get Version"
kexeccmd = os.popen(kcmd).read().split()
kexeccmd.remove("Version")

# Packages to be implemented
#print(f"Shell: {psutil.Process().parent().exe()}")

# Display Resoulution
cmd = "wmic path Win32_VideoController get CurrentVerticalResolution,CurrentHorizontalResolution"
size_tuple = tuple(map(int,os.popen(cmd).read().split()[-2::]))

def terminal():
    try:
        term = os.environ.get('TERM')
        return term
    except KeyError:
        return "Unknown"

# GPU
exec_cmd = "wmic path win32_VideoController get name "
gpu_data = os.popen(exec_cmd).read().split()
gpu_data.remove("Name")

# RAM Usage
ram = psutil.virtual_memory()
tram = ram[0] / 1024 ** 2
aram = ram[4] / 1024 ** 2

print(colored(f"                                  ..,", 'blue'))
print(colored(f"                      ....,,:;+ccllll   ",'blue') + fullname)
print(colored(f"        ...,,+:;  cllllllllllllllllll   ", 'blue') + underscore_list[0])
print(colored(f"  ,cclllllllllll  lllllllllllllllllll   ", 'blue') + f"OS: " + platform.system() + f" {cpu_info['arch']}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + f"Host: " + ' '.join(hostcmd))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + f"Kernel: " + " ".join(kexeccmd))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + f"Uptime: {uptime(0)}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + f"Resolution: {size_tuple[0]}x{size_tuple[1]}")
print("                                        " + f"Terminal: {terminal()}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + f"CPU: {cpu_info['brand_raw']}")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + "GPU: " + " ".join(gpu_data))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue') + f"RAM: {round(aram)} /  {round(tram)}MiB")
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue'))
print(colored(f"  llllllllllllll  lllllllllllllllllll   ", 'blue'))
print(colored(f"  `'ccllllllllll  lllllllllllllllllll   ", 'blue'))
print(colored(f"           `'""*::  :ccllllllllllllllll ", 'blue'))
print(colored(f'                          ````''"*::cll ', 'blue'))
print(colored(f"                                   ``", 'blue'))
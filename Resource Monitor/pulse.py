import psutil as ps
import time 
import os 

while(True):
    os.system('clear')
    print(f"usage: {ps.cpu_percent()}%")
    print(f"frequency: {ps.cpu_freq(percpu=False)}")
    time.sleep(1)
import psutil as ps #for resource monitoring
import time
import subprocess #allows us to execute system wide commands


def main(): #now the code is containerized, not run directly by running the file
    while(True):
 
        subprocess.call("clear")

        subprocess.call("date")

        print(f"usage: {ps.cpu_percent()}%")

        print(f"frequency: {ps.cpu_freq(percpu=False)}")

        time.sleep(1)

if __name__ == "__main__":#checks if the file is being run directly, not imported
    main()

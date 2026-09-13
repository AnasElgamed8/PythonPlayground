bitrate = int(input("Enter the bitrate:\n"))
timestamp = input("Enter the timestamp. eg: 20:14 :\n")
times = timestamp.split(":")
times.reverse()
times = list(map(int, times))

# Seconds
duration = times[0]
# minutes
if len(times) > 1:
    duration += times[1] * 60
# hours
if len(times) > 2:
    duration += times[2] * 60 * 60

total_mbits = duration * bitrate
total_mbytes = total_mbits / 8
print(
    f"This video will use {total_mbytes}Mb, which means {total_mbytes / duration} Mb/s"
)

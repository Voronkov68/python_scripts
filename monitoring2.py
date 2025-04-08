import psutil #библеотека для получения метрик с хоста 
import time

while True:
    print("CPU:", psutil.cpu_percent(interval=1), "%")
    print("RAM:", psutil.virtual_memory().percent, "%")
    print("Disk:", psutil.disk_usage('/').percent, "%")
    print("Net:", psutil.net_io_counters().bytes_sent, "bytes sent")
    print("="*20)
    time.sleep(5)

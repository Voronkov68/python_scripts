import psutil
import time

def get_system_load():
    # Получаем загрузку CPU (в процентах)
    cpu = psutil.cpu_percent(interval=1)
    
    # Получаем использование памяти
    memory = psutil.virtual_memory().percent
    
    # Получаем использование диска
    disk = psutil.disk_usage('/').percent
    
    return cpu, memory, disk

def monitor():
    while True:
        cpu, memory, disk = get_system_load()
        print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
        time.sleep(5)  # проверка каждые 5 секунд

if __name__ == "__main__":
    monitor()

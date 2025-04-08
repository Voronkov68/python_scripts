import subprocess

hosts = ["8.8.8.8", "8.8.4.4", "yandex.ru"]
for host in hosts:
    result = subprocess.run(["ping", "-c", "1", host], stdout=subprocess.DEVNULL) #stdout=subprocess.DEVNULL не выводить результат пинга нак консоль а просто сохранить код ответа
    print(f"{host}: {'OK' if result.returncode == 0 else 'FAIL'}")

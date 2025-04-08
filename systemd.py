import subprocess #библиотека которая позволяет выполнять системные команды из python

services = ["nginx", "docker", "ssh"] #тут перечислены сервисы которые я хочу проверить
for s in services:
    result = subprocess.run(["systemctl", "is-active", s], capture_output=True, text=True) #subprocess -команда, которая запускает внешнюю программу, capture_output=True - сохр вывод в перемен, text=True- вывести результат в строке.
    print(f"{s}: {result.stdout.strip()}")
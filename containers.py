import docker

client = docker.from_env() #создание клиента докер
for c in client.containers.list(): #получаем список запущенных контейнеров
    print(f"{c.name}: {c.status}")

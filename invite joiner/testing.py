import random
with open('proxies.txt', 'r') as proxies:
    proxylist = proxies.readlines()

prox = proxylist[random.randint(0, len(proxylist)-1)]
username = prox.split(":")[-2]
password = prox.split(":")[-1]
port = prox.split(":")[-3]
ip = prox.split(":")[0]
print(username, password, ip, port)
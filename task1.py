# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
# сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции
# ip_address().
import ipaddress
import os
from pprint import pprint
import subprocess

_list = ['77.88.55.55', '1', '178.0.0.500', '64.233.165.104', '8.8.8.8', 'wqwrrw', 'yandex.ru', '0.0.0.1']
ip_list = []


def host_ping(str_list):
    for i in str_list:
        try:
            ip = ipaddress.ip_address(i)
            param = '-n' if os.name == 'nt' else '-c'
            response = subprocess.Popen(["ping", param, '1', str(i)], stdout=subprocess.PIPE)
            if response.wait() == 0:
                # result = f'{ip}, доступен'
                result = {'доступен': str(ip)}
            else:
                # result = f'{ip},не доступен'
                result = {'не доступен': str(ip)}
            ip_list.append(result)
        except Exception as err:
            print(err)
            param = '-n' if os.name == 'nt' else '-c'
            response = subprocess.Popen(["ping", param, '1', str(i)], stdout=subprocess.PIPE)
            if response.wait() == 0:
                result = 'узел доступен'
            else:
                result = 'узел не доступен'
            ip_list.append(f'{str(i)} Не является IP-адресом, {result}')
    return ip_list


if __name__ == '__main__':
    pprint(host_ping(_list))

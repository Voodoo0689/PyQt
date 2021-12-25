import ipaddress
from pprint import pprint

from task1 import host_ping

start_ip = (input("Введите первоначальный адрес c которого начнётся проверка: "))
dia = int(input("Введите количество адресов для проверки: "))
first_oct = start_ip.rsplit('.', 1)[0]
print(f'Проверка {first_oct}._')
last_oct = int(start_ip.split('.')[3])
list_ip = []



def host_range_ping(last_oct):
    oct = 256 - last_oct
    if oct > dia:
        # oct = 256 - last_oct
        print(f'Всего будет проверенно {dia} адресов')
        for i in range(dia):
            list_ip.append(f'{first_oct}.{(str(last_oct + i))}')
        print(list_ip)
        return host_ping(list_ip)
    else:
        print('Не коректный диапазон адресов')


if __name__ == "__main__":
    pprint(host_range_ping(last_oct))

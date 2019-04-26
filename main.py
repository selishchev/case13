from case13 import *

lst_of_rooms = []
lst_of_requests = []

booking = open('booking.txt', 'r')
v = booking.readlines()
for line in v:
    line = line.split(' ')
    fio_demo = [line[1], line[2], line[3]]
    fio = ' '.join(fio_demo)
    lst_of_requests.append(Request(line[0], fio, line[4], line[5], line[6], line[7]))
booking.close()

for i in lst_of_requests:
    print(i)

fund = open('fund.txt', 'r')
m = fund.readlines()
for line in m:
    line = line.split(' ')
    lst_of_rooms.append(Room(line[0], line[1], line[2], line[3]))
fund.close()

for j in lst_of_rooms:
    print(j)

def customer_consent():
    pass


for i in lst_of_requests:
    print('Поступила заявка на бронирование:\n')
    print(i)
    print('\n')
    print('Найден:\n')
    print()  # Например: номер 10 одноместный стандарт раcсчитан на 1 чел. фактически 1 чел. без питания
    # стоимость 2900.00 руб./сутки
    if customer_consent():
        print('Клиент согласен. Номер забронирован.\n')
    else:
        print('Клиент отказался от варианта.\n')

from case13 import *

lst_of_rooms = []
lst_of_requests = []

booking = open('booking.txt', 'r', encoding='utf-8')
v = booking.readlines()
for line in v:
    line = line.split(' ')
    fio_demo = [line[1], line[2], line[3]]
    fio = ' '.join(fio_demo)
    lst_of_requests.append(Request(line[0], fio, line[4], line[5], line[6], line[7].replace('\n', '')))
booking.close()

for i in lst_of_requests:
    print(i)

fund = open('fund.txt', 'r', encoding='utf-8')
m = fund.readlines()
for line in m:
    line = line.split(' ')
    lst_of_rooms.append(Room(line[0], line[1], line[2], line[3].replace('\n', '')))
fund.close()

for j in lst_of_rooms:
    print(j)
    print(j.count_price())


def customer_consent():
    pass


for i in lst_of_requests:
    final_cost = 0
    # Отбор комнат, ровно подходящих по количеству человек
    lst_of_suitable_rooms = []
    for rm in lst_of_rooms:
        if i.get_amount_of_people() == rm.get_capacity():
            lst_of_suitable_rooms.append(rm)
    # Подсчет максимальной стоимости за номер в зависимости от бюджета клиента
    # Тут еще нужно сделать бронь оптимального номера на запрошенные даты
    if lst_of_suitable_rooms:
        lst_of_costs = []
        for k in lst_of_suitable_rooms:
            cost = k.count_price()
            difference = i.get_money() - cost
            if difference > 999:
                cost += meal['полупансион']
            elif difference > 279:
                cost += meal['завтрак']
            if i.get_money() > cost:
                lst_of_costs.append(cost)
        if lst_of_costs:
            final_cost = max(lst_of_costs)
            print(final_cost)
    else:
        pass

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

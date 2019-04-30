from case13 import *
import random
import operator
import datetime


def add_date(arrival_date, days, k):
    dt = datetime.datetime.strptime(arrival_date, "%d.%m.%Y").date()
    rmn = 0
    for rm in hotel:
        if (rmn + 1) == int(k.room_number):
            for j in range(int(days)):
                newdt = dt + datetime.timedelta(days=j)
                rm.append(newdt)
            break
        rmn += 1


def valid_date(arrival_date, days, k):
    dt = datetime.datetime.strptime(arrival_date, "%d.%m.%Y").date()
    is_valid = True
    rmn = 0
    for rm in hotel:
        if (rmn + 1) == int(k.room_number):
            for j in range(int(days)):
                newdt = dt + datetime.timedelta(days=j)
                for dd in rm:
                    if newdt == dd:
                        is_valid = False
                        break
        if is_valid is False:
            break
        rmn += 1
    return is_valid


def setroom(i, hotel):
    num_room = None
    kc = 0
    for k in lst_of_rooms:
        if k.capacity == i.amount_of_people:
            if valid_date(i.arrival_date, i.days, k):
                if int(i.money) >= k.count_price():
                    num_room = k
                    add_date(i.arrival_date, i.days, k)
                    break
        kc += 1
    return num_room


def get_free_room(i):
    num_room = None
    for k in lst_of_rooms:
        if k.capacity >= i.amount_of_people:
            if valid_date(i.arrival_date, i.days, k):
                if int(i.money) >= k.count_discount_price():
                    num_room = k
                    add_date(i.arrival_date, i.days, k)
                    break
    return num_room


def get_rooms_stat(arrival_date):
    stat = ""
    cnt_1 = 0
    cnt_2 = 0
    cnt_half_luxe = 0
    cnt_luxe = 0
    cnt_all_1 = 0
    cnt_all_2 = 0
    cnt_all_half_luxe = 0
    cnt_all_luxe = 0
    dt = datetime.datetime.strptime(arrival_date, "%d.%m.%Y").date()
    for room in lst_of_rooms:
        rmn = 0
        if str(room.type_of_room) == "одноместный":
            cnt_all_1 += 1
        else:
            if str(room.type_of_room) == "двухместный":
                cnt_all_2 += 1
            else:
                if str(room.type_of_room) == "полулюкс":
                    cnt_all_half_luxe += 1
                else:
                    if str(room.type_of_room) == "люкс":
                        cnt_all_luxe += 1
        for rm in hotel:
            if (rmn + 1) == int(room.room_number):
                    for dd in rm:
                        if dt == dd:
                            if str(room.type_of_room) == "одноместный":
                                cnt_1 += 1
                            else:
                                if str(room.type_of_room) == "двухместный":
                                    cnt_2 += 1
                                else:
                                    if str(room.type_of_room) == "полулюкс":
                                        cnt_half_luxe += 1
                                    else:
                                        if str(room.type_of_room) == "люкс":
                                            cnt_luxe += 1

            rmn += 1
    cnt_room_all = cnt_all_1 + cnt_all_2 + cnt_all_half_luxe + cnt_all_luxe
    cnt_room_busy = cnt_1 + cnt_2 + cnt_half_luxe + cnt_luxe
    percent = round(cnt_room_busy * 100 / cnt_room_all, 2)
    stat += "Количество занятых номеров: " + str(cnt_room_busy) + "\n"
    stat += "Количество свободных номеров: " + str(cnt_room_all - cnt_room_busy) + "\n"
    stat += "Процент загруженности гостиницы: " + str(percent) + "%\n"
    stat += "Занятость по категориям:" + "\n"
    stat += "Одноместных: " + str(cnt_1) + " из " + str(cnt_all_1) + "\n"
    stat += "Двухместных: " + str(cnt_2) + " из " + str(cnt_all_2) + "\n"
    stat += "Полулюкс: " + str(cnt_half_luxe) + " из " + str(cnt_all_half_luxe) + "\n"
    stat += "Люкс: " + str(cnt_luxe) + " из " + str(cnt_all_luxe) + "\n"

    income = 0
    for i in all_sum_sorted:
        if i.date == arrival_date:
            income = income + int(i.money)
    stat += "Доход: " + str(income) + "\n"

    lost = 0
    for i in lost_sum_sorted:
        if i.date == arrival_date:
            lost = lost + int(i.money)
    stat += "Упущенный доход: " + str(lost) + "\n"

    return stat


all_sum = []
lost_sum = []
lst_empty_rooms = []
lst_of_rooms = []
lst_of_discount_rooms = []
lst_of_full_rooms = []
lst_of_requests = []
booking = open('booking.txt', 'r', encoding='utf-8')
v = booking.readlines()
for line in v:
    line = line.split(' ')
    count_days = int((line[6]))
    date_in = line[5].split(".")
    day_out = int(date_in[0])+count_days
    fio_demo = [line[1], line[2], line[3]]
    fio = ' '.join(fio_demo)
    lst_of_requests.append(Request(line[0], fio, line[4], line[5], line[6], line[7].replace('\n', '')))
booking.close()

sort_lst_of_requests = sorted(lst_of_requests, key=operator.attrgetter('date_of_booking'))
fund = open('fund.txt', 'r', encoding='utf-8')
m = fund.readlines()
for line in m:
    line = line.split(' ')
    lst_of_rooms.append(Room(line[0], line[1], line[2], line[3].replace('\n', '')))
fund.close()

hotel = []
for j in lst_of_rooms:
    for i in range(len(lst_of_rooms)):
        room = []
        hotel.append(room)

dt = ""
for i in sort_lst_of_requests:
    dt = i.date_of_booking
    break
all_dates = []
dates = []
for i in sort_lst_of_requests:
    if i.date_of_booking == dt:
        dates.append(i)
    else:
        all_dates.append(dates)
        dates = []
        dates.append(i)
        dt = i.date_of_booking
all_dates.append(dates)

for j in range(len(all_dates)):
    for i in all_dates[j]:
        print("Поступила заявка на бронирование: ")
        print(i)
        r = setroom(i, hotel)
        if r is None:
            r2 = get_free_room(i)
            if r2 is None:
                lost_sum.append(Calc(i.arrival_date, i.money))
                print("Предложений по данному запросу нет. В бронировании отказано.\n")
            else:
                print("Подобран номер со скидкой:")
                print(r2)
                cost = r2.count_discount_price()
                difference = i.get_money() - cost
                if difference > 999:
                    cost += meal['полупансион']
                    print('Тип питания: полупансион')
                elif difference > 279:
                    cost += meal['завтрак']
                    print('Тип питания: завтрак')
                else:
                    print('Тип питания: без питания')
                print('Стоимость ' + str(cost) + ' руб./сутки\n')
                all_sum.append(Calc(i.arrival_date, cost))
                random_value = random.randint(1, 100)
                if random_value > 25:
                    print('Клиент согласен. Номер забронирован\n')
                else:
                    lost_sum.append(Calc(i.arrival_date, i.money))
                    print('Клиент отказался от варианта\n')
        else:
            print("Найден:")
            print(r)
            cost = r.count_price()
            difference = int(i.get_money()) - cost
            if difference > 999:
                cost += meal['полупансион']
                print('Тип питания: полупансион')
            elif difference > 279:
                cost += meal['завтрак']
                print('Тип питания: завтрак')
            else:
                print('Тип питания: без питания')
            print('Стоимость ' + str(cost) + ' руб./сутки\n')
            all_sum.append(Calc(i.arrival_date, cost))
            print('Клиент согласен. Номер забронирован\n')
    all_sum_sorted = sorted(all_sum, key=operator.attrgetter('date'))
    lost_sum_sorted = sorted(lost_sum, key=operator.attrgetter('date'))

    print("*********************** Итог за " + str(i.date_of_booking) + " **************************")
    print(get_rooms_stat(i.date_of_booking))
    print("*********************************************************************")

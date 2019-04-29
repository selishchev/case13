from case13 import *
import random
import datetime
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
        if is_valid == False:
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

# Сортируем по дате бронирования, дате заселения, количеству человек и бюджету.
sort_lst_of_requests = sorted(lst_of_requests, key=operator.attrgetter('date_of_booking', 'arrival_date',
                                                                       'amount_of_people', 'money'))
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

#Ищем первую дату бронирования
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
        if (r  == None):
            r2 = get_free_room(i)
            if r2 == None:
                print("Подходящий номер найти не удалось!")
            else:
                print("Подобран номер со скидкой:")
                print(r)
        else:
            print("Номер забронирован:")
            print(r)


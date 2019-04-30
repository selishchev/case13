room = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
coefs = {'стандарт': 1.0, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
meal = {'без питания': 0, 'завтрак': 280, 'полупансион': 1000}


class Room:
    def __init__(self, room_number, type_of_room, capacity, comfort_level):
        self.room_number = room_number
        self.type_of_room = type_of_room
        self.capacity = capacity
        self.comfort_level = comfort_level

    def __str__(self):
        s = 'Номер комнаты: ' + str(self.room_number) + '\n'
        s += 'Тип номера: ' + str(self.type_of_room) + '\n'
        s += 'Максимальная вместимость (кол-во человек): ' + str(self.capacity) + '\n'
        s += 'Степень комфортности: ' + str(self.comfort_level)
        return s

    def __repr__(self):
        return self.__str__()

    def count_price(self):
        price2 = room[self.type_of_room] * coefs[self.comfort_level]
        return int(price2)

    def get_capacity(self):
        return self.capacity

    def count_discount_price(self):
        discount_price = room[self.type_of_room] * coefs[self.comfort_level] * 0.7
        return int(discount_price)


class Request:

    def __init__(self, date_of_booking, full_name, amount_of_people, arrival_date, days, money):
        self.date_of_booking = date_of_booking
        self.full_name = full_name
        self.amount_of_people = amount_of_people
        self.arrival_date = arrival_date
        self.days = days
        self.money = money

    def __str__(self):
        s = 'Дата бронирования: ' + str(self.date_of_booking) + '\n'
        s += 'ФИО: ' + str(self.full_name) + '\n'
        s += 'Количество человек: ' + str(self.amount_of_people) + '\n'
        s += 'Дата въезда: ' + str(self.arrival_date) + '\n'
        s += 'Количество суток: ' + str(self.days) + '\n'
        s += 'Максимальная сумма на человека в сутки: ' + str(self.money) + '\n'
        return s

    def __repr__(self):
        return self.__str__()

    def get_amount_of_people(self):
        return self.amount_of_people

    def get_money(self):
        return int(self.money)

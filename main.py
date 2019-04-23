lst_of_rooms = []
lst_of_requests = []


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

number_of_tickets = int(input('Сколько билетов желаете приобрести?\n'))
total_sum = 0
sale = 0
for r in range(number_of_tickets):
    age = int(input('Укажите возраст: \n'))
    if 0 < age < 18:
        total_sum += 0
    elif 18 <= age < 25:
        total_sum += 990
    elif age >= 25:
        total_sum += 1390
    else:
        print('Некорректный возраст')

if number_of_tickets > 3:
    total_sum *= 0.9
    print('Стоимость к оплате c учетом 10% скидки', total_sum)
else:
    print('Стоимость к оплате: ', total_sum)
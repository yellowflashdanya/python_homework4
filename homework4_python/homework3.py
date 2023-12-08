meters = int(input('Введіть кількість метрів: '))
print('1. Конвертувати метри у милі.')
print('2. Конвертувати метри у дюйми.')
print('3. Конвертувати метри у ярди.')
choice = input('Виберіть номер операції: ')
if choice == '1':
    print(meters, 'метрів =', meters * 0.00062137, 'миль')
if choice == '2':
    print(meters, 'метрів =', meters * 39.370, 'дюймів')
if choice == '3':
    print(meters, 'метрів =', meters * 1.0936, 'ярдів')

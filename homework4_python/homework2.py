number1 = int(input('Введіть перше число: '))
number2 = int(input('Введіть друге число: '))
number3 = int(input('Введіть третє число: '))

print('1. Вибрати максимум із трьох чисел. ')
print('2. Вибрати мінімум із трьох чисел. ')
print('3. Визначити середнє арифметичне трьох чисел. ')

choice = input('Виберіть номер операції >>> ')
if choice == '1':
    if number1 <= number2 <= number3:
        print(number3)
    if number2 <= number1 <= number3:
        print(number3)
    if number1 <= number3 <= number2:
        print(number2)
    if number3 <= number1 <= number2:
        print(number2)
    if number2 <= number3 <= number1:
        print(number1)
    if number3 <= number2 <= number1:
        print(number1)

if choice == '2':
    if number1 <= number2 <= number3:
        print(number1)
    if number1 <= number3 <= number2:
        print(number1)
    if number2 <= number1 <= number3:
        print(number2)
    if number2 <= number3 <= number2:
        print(number2)
    if number3 <= number2 <= number1:
        print(number3)
    if number3 <= number1 <= number2:
        print(number3)

if choice == '3':
    print(float((number1 + number2 + number3) / 3))




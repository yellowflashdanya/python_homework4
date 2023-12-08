firstNumber = int(input('Введіть перше число >>> '))
secondNumber = int(input('Введіть друге число >>> '))
thirdNumber = int(input('Введіть третє число >>> '))
print('1. Сума 3х чисел')
print('2. Добуток 3х чисел')
choice = input('Виберіть операцію: ')
sum = firstNumber + secondNumber + thirdNumber
product = firstNumber * secondNumber * thirdNumber
if choice == '1':
    print(sum)
elif choice == '2':
    print(product)
else:
    print('Error')



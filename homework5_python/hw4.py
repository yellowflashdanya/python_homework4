n1 = int(input('Введіть перше число >>> '))
n2 = int(input('Введіть друге число >>> '))
if n1 != n2 and n1 > n2:
    print(n2, n1)
elif n1 != n2 and n1 < n2:
    print(n1, n2)
elif n1 == n2:
    print('Числа є рівними!')
else:
    print('Error!')
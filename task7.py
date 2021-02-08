amount_number = 0
quantity_number = 0
quantity_even = 0
quantity_not_even = 0
max = 0
min = 0

while True:
    number = int(input('Введите целое число: '))
    if number == 0:
        break
    amount_number += number
    quantity_number += 1
    if number % 2 == 0:
        quantity_even += 1
    if number % 2 != 0:
        quantity_not_even += 1
    if max == number and min == number:
        max = number
        min = number
    if number > max:
        max = number
    if number < min:
        min = number
print ('Сумма чисел: ' + str(amount_number))
print ('Количество чисел: '+ str(quantity_number))
print ('Среднее арифметическое чисел: ' + str(amount_number/quantity_number))
print('Количество четных: ' + str(quantity_even))
print ('Количество не четных: ' + str(quantity_not_even))
print ('Максимальное значение: ' + str(max))
print ('Минимальное значение: ' + str(min))











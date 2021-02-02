number = int(input('Введите число: '))
value = 1
while number > 0:
    print (value**2)
    value += 1
    if value**2 > number:
        break

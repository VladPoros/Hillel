number = int(input('Введите число: '))
value = 1
degree = -1
value_degree = 0
while number > 0:
    value_degree = value
    degree += 1
    value *= 2
    if value > number:
        break
print(degree, value_degree)

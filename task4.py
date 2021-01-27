a = int(input('Введите число: '))
n1 = a % 10
n2 = (a//10)%10
n3 = a//100
aNew = str(n1)+str(n2)+str(n3)
print ('Перевернутное число:'+ aNew)

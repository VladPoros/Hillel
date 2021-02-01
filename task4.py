a = int(input('Введите число: '))
n1 = a % 10
n2 = (a//10)%10
n3 = a//100
a_new = (n1*10+n2)*10+n3
print (a_new)
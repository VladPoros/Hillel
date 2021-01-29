# ввод данных
pupils = int(input ('Количество школьников: '))
apples = int(input ('Количество яблок: '))
# поиск кол-во яблок для каждоко школьника поровну и остаток в корзине
apples_pupils = apples//pupils
excess_apples = apples % pupils
# вывод результата
print ('Яблок достанется каждому школьнику: ' + str(apples_pupils))
print ('Яблок останется в корзине: ' + str(excess_apples))
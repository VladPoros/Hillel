file = open('src_14.txt', encoding='utf-8')
newList = []
for line in file:
     res = line.replace('\t',' ').split()
     newList.append(res)

for i in newList:
    sum_el = 0
    count = 0
    for j, number in enumerate(i):
        if j >= 2:
            sum_el = sum_el + int(number)
            count +=1
            i[2] = round(sum_el/count, 2)
print(newList)

pointList = []
for i in newList:
    if i[2] < 5:
        s = [i[1], i[0], i[2]]
        pointList.append(s)
print(pointList)

sum_points = 0
stud_count = 0

for i in newList:
    sum_points += i[2]
    stud_count +=1
    mid_stud_points = round(sum_points/stud_count, 2)
print('Средний балл по классу: ' + str(mid_stud_points))


file = open('point_sudents.txt', 'w', encoding='utf-8')

for i in newList:
    s = [i[1], ' ' + i[0][:1] + '.', '{:>10}'.format(i[2])]
    for line in s:
        file.write(line)
    file.write('\n')
file.close()


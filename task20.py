from random import randint
lst = []
lst2 = []
m = int(input())
n = int(input())
print()
for i in range (m):
        lst.append([randint(1, 50) for _ in range(n)])

def tabl (array, array2):
    for i in array:
        for j in i:
            print('{:<3}'.format(j), end=' ')
        print()
    print()
    for i in array2:
        print('{:<3}'.format(i), end=' ')
    print()
for i in range(m):
    sum_el = 0
    for j in range(n):
        sum_el = sum_el + lst[i][j]
    s = '\t'+ str(sum_el)
    lst[i].append(s)

for i in range(n):
    sum_el = 0
    for j in range(m):
        sum_el = sum_el + lst[j][i]
    lst2.append(sum_el)

tabl(lst, lst2)
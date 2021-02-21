from random import randint
lst = []
lst2 = []
m = int(input())
print()
for i in range (m):
    lst.append([randint(1, 50) for _ in range(m)])
def tabl (array, array2):
    for i in array:
        for j in i:
            print('{:<3}'.format(j), end=' ')
        print()
    for i in array2:
        print('{:<3}'.format(i), end=' ')
    print()
for i in range(len(lst)):
    sum_el = 0
    for j in range(len(lst)):
        sum_el = sum_el + lst[j][i]
    lst2.append(sum_el)
def bubble_sort(array, array2):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                for x in range(len(array2)):
                    array2[x][j], array2[x][j+1] = array2[x][j+1], array2[x][j]
    for i in range(len(array2)-1):
        for j in range(len(array2)-1-i):
            for x in range(len(array2)):
                if array2[j][x] > array2[j + 1][x] and (x+1) %2 == 0:
                    array2[j][x], array2[j + 1][x] = array2[j + 1][x], array2[j][x]
                if array2[j][x] < array2[j + 1][x] and (x+1) % 2 != 0:
                    array2[j][x], array2[j + 1][x] = array2[j + 1][x], array2[j][x]

tabl(lst, lst2)
print()
bubble_sort(lst2, lst)
tabl(lst,lst2)
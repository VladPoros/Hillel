from random import randint
lst = [randint(160, 200) for _ in range(20)]
print(lst)
lst.sort(reverse=True)
print(lst)
x = int(input())
n = 0
for i in range(len(lst)):
    if lst[i] >= x:
        n += 1
print(n+1)

from random import randint
lst = [randint(1, 50) for _ in range(20)]
print(lst)
quantity = 0
for i in range(1, len(lst)-1):
    if  lst[i-1] < lst[i] > lst[i+1]:
        quantity += 1
        print(lst[i], end=' ')
print()
print(quantity)

from random import randint
lst = [randint(1, 20) for _ in range(20)]
print(lst)
k = 7
print(lst[k])
for i in range(k, len(lst)-1):
     lst[i] = lst[i+1]

lst.pop()
s = ' '.join([str(i) for i in lst])
print(s)

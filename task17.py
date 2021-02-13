h = int(input())
w = h*2 - 1
for i in range(h):
    for j in range(w):
        if (
                i == h-1
                or j == h - i - 1
                or j == h + i - 1
        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()

print()

h2= int(input())
w2 = h2*2 - 1

for i in range(h2):
    for j in range(w2):
        if j <= h2 + i - 1 and j >= h2 - i- 1:
            print('*  ', end = '')
        else:
            print('   ', end='')
    print()

print()

h3= int(input())

for i in range(h3):
    for j in range(h3):
        if (
                i <= h3//2 and j <= h3//2 + i and j >= h3//2 - i
                or (i >= h3//2 and j==i-h3//2)
                or (i >= h3//2 and j == h3 - i + h3//2 - 1)

        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()

print()

h4= int(input())

for i in range(h4):
    for j in range(h4):
        if (
                i <= h4//2 and j <= h4//2 + i and j >= h4//2 - i
                or (i >= h4//2 and j==i-h4//2)
                or (i >= h4//2 and j == h4 - i + h4//2 - 1)
                or (i >= h4//2 and j == h4//2 )

        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
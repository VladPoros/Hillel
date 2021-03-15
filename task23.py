class Counter:

    def __init__(self, min_val, max_val, num):
        self.min_val = min_val
        self.max_val = max_val
        self.num = num

    def increase (self):
        if self.num < self.min_val:
            self.min_val = self.num

        if self.num >= self.max_val:
            self.max_val = self.num

        if self.num == self.max_val:
            self.num = self.min_val
            return self.num

        while self.num < self.max_val:
            self.num += 1
            return self.num


val_1 = int(input('Enter first value of the counter: '))
val_2 = int(input('Enter first value of the counter: '))
val_3 = input('Enter value of current position of the counter: ')

if val_3 == '':
    val_3 = val_1
else:
    val_3 = int(val_3)

count = Counter(val_1, val_2, val_3)

print('Present value of the counter: ' + str(count.increase()))
print('Present value of the counter: ' + str(count.increase()))
print('Present value of the counter: ' + str(count.increase()))

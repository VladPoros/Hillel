class Buffer:
    def __init__(self):
        self.val = []

    def add(self, *a):
        self.val.extend(a)

    def get_current_part(self):
        while self.val > self.val[:4]:
            print(sum(self.val[:5]))
            del self.val[0:5]
        return self.val


amount = Buffer()
amount.add(2, 3, 1, 8, 4, 5)
amount.get_current_part()
amount.add(1, 1, 3, 2, 0)
amount.get_current_part()
amount.add(1, 1)
amount.get_current_part()
amount.add(10, 1)
amount.get_current_part()

lst =[
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

res = tuple(map(lambda i: (i[0], round(i[2]*i[3] if i[2]*i[3]> 100 else i[2]*(i[3]+10), 2)),  lst))
print (list(res))
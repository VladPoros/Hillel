s1 = input ()
s2 = s1[0: 1:]
s3 = s1[-1: ]
s4 = s1[1: -1:]
s5 = s4.replace('h', 'H')

s_finish = s2 + s5 + s3

print(s_finish)

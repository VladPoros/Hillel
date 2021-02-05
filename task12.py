s = input()
ch = input()
ch_total = -1
for _ in s:
    ch_total = s.find (ch, ch_total + 1)
    if ch_total == -1:
        break
    print (ch_total)

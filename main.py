count = int(0)
for i in range(1,1000000,1):
    d6 = int((i / 100000) % 10)
    d5 = int((i / 10000) % 10)
    d4 = int((i / 1000) % 10)
    d3 = int((i / 100) % 10)
    d2 = int((i / 10) % 10)
    d1 = int(i % 10)
    raz = d1 + d2 + d3
    dva = d4 + d5 + d6
    if raz == dva:
        count += 1
print(count)

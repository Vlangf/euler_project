max_count = {}
for i in range(2, 999999):
    count = 0
    o = i
    while o != 1:
        if o % 2 == 0:
            o = o / 2
            count += 1
        else:
            o = 3 * o + 1
            count += 1
    max_count[i] = count

m = max(max_count.values())
for k, v in max_count.items():
    if v == m:
        print(k)
        print(v)
        break

with open("day6.input") as f:
    lines = f.readlines()

    chars = [{} for _ in range(8)]
    for line in lines:
        for i, ch in enumerate(line.strip()):
            d = chars[i]
            if ch not in d:
                d[ch] = 1
                continue
            d[ch] += 1

    # print chars

    for i, d in enumerate(chars):
        for k, v in d.iteritems():
            if v > 23:
                print i, k

    print

    for i, d in enumerate(chars):
        for k, v in d.iteritems():
            if v < 23:
                print i, k

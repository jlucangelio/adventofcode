import sys

# Disc #1 has 13 positions; at time=0, it is at position 1.
# Disc #2 has 19 positions; at time=0, it is at position 10.
# Disc #3 has 3 positions; at time=0, it is at position 2.
# Disc #4 has 7 positions; at time=0, it is at position 1.
# Disc #5 has 5 positions; at time=0, it is at position 3.
# Disc #6 has 17 positions; at time=0, it is at position 5.


def chinese_remainder(n, a):
    s = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


discs = {}

with open(sys.argv[1]) as f:
    lines = f.readlines()

    for line in lines:
        tokens = line.strip().split()
        discnum = int(tokens[1][1:])
        npositions = int(tokens[3])
        starting_pos = int(tokens[11][:-1])

        print discnum, "npositions", npositions, "starting_pos", starting_pos
        discs[discnum] = (npositions, starting_pos)

print

delays = []

for i in range(1, len(discs) + 1):
    npos, start = discs[i]

    delay = (npos - (start + i)) % npos
    if delay == 0:
        delay = npos
    print i, "delay", delay
    delays.append(delay)

# print lcmm(delays)

delay = 0
while True:
    if all([delay % discs[i][0] == delays[i-1] for i in range(1, len(discs) + 1)]):
        print delay
        break
    delay += 1
    if delay % 100000 == 0:
        print delay

print chinese_remainder([discs[i][0] for i in range(1, len(discs) + 1)], delays)

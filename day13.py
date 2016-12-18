from copy import copy
import sys

FAV = 1352
# FAV = 10

TARGET = (31, 39)
# TARGET = (7, 4)

def is_open(pos):
    # Find x*x + 3*x + 2*x*y + y + y*y.
    # Add the office designer's favorite number (your puzzle input).
    # Find the binary representation of that sum; count the number of bits that are 1.
    # If the number of bits that are 1 is even, it's an open space.
    # If the number of bits that are 1 is odd, it's a wall.
    x, y = pos
    n = x*x + 3*x + 2*x*y + y*y + y + FAV
    b = format(n, "b")
    numsetbits = sum([int(digit) for digit in b])
    return numsetbits % 2 == 0

initial = (1, 1)
level = 0
current_set = set([initial])
next_set = set([])
all_set = set([initial])
found = False

for _ in range(50):
    if TARGET in current_set:
        print level
        found = True
        break

    # print current_set
    for pos in current_set:
        x, y = pos

        if x > 0:
            left = (x - 1, y)
            if is_open(left):
                next_set.add(left)

        right = (x + 1, y)
        if is_open(right):
            next_set.add(right)

        if y > 0:
            up = (x, y - 1)
            if is_open(up):
                next_set.add(up)

        down = (x, y + 1)
        if is_open(down):
            next_set.add(down)

    level += 1

    current_set = copy(next_set)
    all_set.update(next_set)

print len(all_set)
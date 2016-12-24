import sys

from copy import copy

###########
#0.1.....2#
#.#######.#
#4.......3#
###########

LEVELS = 1000
MAX_DIGIT = 0

xs = 0
ys = 0
m = []
initial = None
with open(sys.argv[1]) as f:
    for j, line in enumerate(f.readlines()):
        line = line.strip()
        if j == 0:
            xs = len(line)
            m =[["#"] for _ in range(xs)]
            ys += 1
            continue

        for i, c in enumerate(line):
            if c == "0":
                initial = (i, j)
            if c != "#" and c != ".":
                intc = int(c)
                if intc in range(10) and intc > MAX_DIGIT:
                    MAX_DIGIT = int(c)
            m[i].append(c)
        ys += 1

print MAX_DIGIT
DIGITS = set([str(d) for d in xrange(MAX_DIGIT + 1)])
print DIGITS

def found(digits_seen, map_position):
    is_found = False
    seen = set(digits_seen)
    if map_position in DIGITS:
        if map_position != "0" or len(seen) == len(DIGITS) - 1:
            seen.add(map_position)
    if len(seen) == len(DIGITS):
        is_found = True
    return (seen, is_found)

level = 0
prev_set = set()
# current_set = {(initial, frozenset("0"))}
current_set = {(initial, frozenset())}
next_set = set()
was_found = False

for i in range(LEVELS):
    print "level", i, len(current_set)
    # print current_set
    # print
    if was_found:
        break

    for state in current_set:
        if was_found:
            break

        ((sx, sy), seen) = state
        # if len(seen) == len(DIGITS) - 1:
        #     print len(seen)

        newx = sx - 1
        left = (newx, sy)
        map_left = m[newx][sy]
        if map_left != "#":
            digits_seen, was_found = found(seen, map_left)
            state_left = (left, frozenset(digits_seen))

            if state_left not in prev_set:
                next_set.add(state_left)

        newx = sx + 1
        right = (newx, sy)
        map_right = m[newx][sy]
        if map_right != "#":
            digits_seen, was_found = found(seen, map_right)
            state_right = (right, frozenset(digits_seen))

            if state_right not in prev_set:
                next_set.add(state_right)

        newy = sy - 1
        up = (sx, newy)
        map_up = m[sx][newy]
        if map_up != "#":
            digits_seen, was_found = found(seen, map_up)
            state_up = (up, frozenset(digits_seen))

            if state_up not in prev_set:
                next_set.add(state_up)

        newy = sy + 1
        down = (sx, newy)
        map_down = m[sx][newy]
        if map_down != "#":
            digits_seen, was_found = found(seen, map_down)
            state_down = (down, frozenset(digits_seen))

            if state_down not in prev_set:
                next_set.add(state_down)

    level += 1

    # if next_set == current_set:
    #     break

    prev_set = copy(current_set)
    current_set = copy(next_set)
    next_set = set()

print level

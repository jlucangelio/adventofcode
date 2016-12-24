import itertools
import random
import sys

from copy import copy

# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.

def rotate(s, steps, left=True):
    if left:
        return s[steps:] + s[:steps]
    else:
        return s[-steps:] + s[:-steps]

def scramble(s, instrs):
    current_pass = copy(s)
    next_pass = copy(s)

    for line in instrs:
        line = line.strip()

        # print current_pass, line
        tokens = line.split()

        if tokens[0] == "swap":
            if tokens[1] == "position":
                px = int(tokens[2])
                py = int(tokens[5])
            elif tokens[1] == "letter":
                lx = tokens[2]
                ly = tokens[5]
                # print lx, ly
                px = current_pass.index(lx)
                py = current_pass.index(ly)
            next_pass[px] = current_pass[py]
            next_pass[py] = current_pass[px]

        elif tokens[0] == "rotate":
            if tokens[1] == "left":
                steps = int(tokens[2])
                next_pass = rotate(current_pass, steps, True)
            elif tokens[1] == "right":
                steps = int(tokens[2])
                next_pass = rotate(current_pass, steps, False)

            elif tokens[1] == "based":
                letter = tokens[6]
                steps = current_pass.index(letter)
                next_pass = rotate(current_pass, 1, False)
                next_pass = rotate(next_pass, steps, False)
                if steps >= 4:
                    next_pass = rotate(next_pass, 1, False)

        elif tokens[0] == "reverse":
            x = int(tokens[2])
            y = int(tokens[4])
            span = current_pass[x:y+1]
            span.reverse()
            next_pass = current_pass[:x] + span + current_pass[y+1:]

        elif tokens[0] == "move":
            index_f = int(tokens[2])
            index_t = int(tokens[5])

            f = current_pass[index_f]

            next_pass = current_pass[:index_f] + current_pass[index_f + 1:]
            if index_t == len(next_pass):
                next_pass.append(f)
            else:
                next_pass = next_pass[:index_t] + [f] + next_pass[index_t:]

        current_pass = copy(next_pass)

    return "".join(current_pass)

INPUT = list("abcde")
INPUT = list("abcdefgh")
current_pass = copy(INPUT)
next_pass = copy(INPUT)

with open(sys.argv[1]) as f:
    lines = f.readlines()

print scramble(INPUT, lines)

for i, s in enumerate(itertools.permutations(list("abcdefgh"))):
    if i % 1000 == 0:
        print i
    l = list(s)
    random.shuffle(l)
    if scramble(l, lines) == "fbgdceah":
        print "".join(l)
        break
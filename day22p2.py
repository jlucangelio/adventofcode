import sys

from copy import copy

# Filesystem              Size  Used  Avail  Use%
# '/dev/grid/node-x0-y0     90T   69T    21T   76%'

xs = 35
ys = 27

USED = 0
AVAIL = 1

TARGET = (0, 0)
SOURCE = (xs - 1, 0)
# SOURCE_AMOUNT = nodes[xs - 1][0][0]

nodes = [[None for _ in range(ys)] for _ in range(xs)]
state = [[None for _ in range(ys)] for _ in range(xs)]

with open(sys.argv[1]) as f:
    lines = f.readlines()

    for line in lines:
        # print line
        node, size, used, avail, percent = line.split()

        used = int(used[:-1])
        avail = int(avail[:-1])

        nodex = int(node.split("-")[1][1:])
        nodey = int(node.split("-")[2][1:])

        nodes[nodex][nodey] = [used, avail]

nviable = 0
for i in range(xs):
    for j in range(ys):
        nodea = (i, j)
        for m in range(xs):
            for n in range(ys):
                nodeb = (m, n)
                if nodea == nodeb:
                    continue

                if nodes[i][j][USED] == 0: # used == 0
                    state[i][j] = "_"
                    continue

                if nodes[i][j][USED] <= nodes[m][n][AVAIL]:    # first.used <= second.avail
                    nviable += 1

                if nodes[i][j][USED] >= 100:
                    state[i][j] = "#"

print nviable

for j in range(ys):
    for i in range(xs):
        if (i, j) == (0, 0):
            print "T",
        elif (i, j) == (xs - 1, 0):
            print "G",
        elif state[i][j] is None:
            print ".",
        else:
            print state[i][j],
    print

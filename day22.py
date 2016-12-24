import sys

# Filesystem              Size  Used  Avail  Use%
# '/dev/grid/node-x0-y0     90T   69T    21T   76%'

xs = 35
ys = 27

nodes = [[None for _ in range(ys)] for _ in range(xs)]


def move(dst_node, src_node, amount):
    src_x, src_y = src_node
    dst_x, dst_y = dst_node

    nodes[dst_x][dst_y][0] += amount    # dst node receives amount, used goes up
    nodes[dst_x][dst_y][1] -= amount    # avail goes down

    nodes[src_x][src_y][0] -= amount    # src node loses amount, used goes down
    nodes[src_x][src_y][1] += amount    # avail goes up


def spread(node, amount):
    nodex, nodey = node
    node_below_avail = nodes[nodex][nodey + 1][1]
    steps = 0
    if node_below_avail < amount:
        steps += spread((nodex, nodey + 1), amount - node_below_avail)

    move((nodex, nodey + 1)(nodex, nodey), amount)
    return steps + 1


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

viable = 0
for i in range(xs):
    for j in range(ys):
        nodea = (i, j)
        for m in range(xs):
            for n in range(ys):
                nodeb = (m, n)
                if nodea == nodeb:
                    continue

                if nodes[i][j][0] == 0: # used == 0
                    continue

                if nodes[i][j][0] <= nodes[m][n][1]:    # first.used <= second.avail
                    viable += 1

print viable
print xs * ys

target = (0, 0)
source = (xs - 1, 0)
source_used = nodes[xs - 1][0][0]
steps = 0
for i in range(1, xs + 1):
    nodex = xs - i
    avail = nodes[nodex - 1][0]
    if source_used > avail:
        steps += spread((nodex - 1, 0), source_used - avail)

    move((nodex, 0), (nodex - 1, 0), source_used)
    steps += 1

print steps

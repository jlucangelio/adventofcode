import sys

def rotate(l, n):
    return l[n:] + l[:n]

def print_screen(screen):
    for j in range(len(screen)):
        for i in range(len(screen[0])):
            if screen[j][i] == True:
                print "#",
            else:
                print ".",
        print
    print

NROWS = 6
NCOLS = 50
SCREEN = [[False for _ in range(NCOLS)] for _ in range(NROWS)]

with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        line = line.strip()

        if line[:4] == "rect":
            _, dims = line.split()
            x, y = dims.split("x")

            for j in range(int(y)):
                for i in range(int(x)):
                    SCREEN[j][i] = True

        elif line[:6] == "rotate":
            tokens = line.split()
            if tokens[1] == "row":
                rowindex = int(tokens[2].split("=")[1])
                npixels = int(tokens[4]) % NCOLS
                SCREEN[rowindex] = rotate(SCREEN[rowindex], -npixels)

            elif tokens[1] == "column":
                colindex = int(tokens[2].split("=")[1])
                npixels = int(tokens[4]) % NROWS

                col = [SCREEN[ridx][colindex] for ridx in range(NROWS)]
                col = rotate(col, -npixels)
                for ridx in range(NROWS):
                    SCREEN[ridx][colindex] = col[ridx]

        print_screen(SCREEN)

    print_screen(SCREEN)
    count = 0
    for j in range(len(SCREEN)):
        for i in range(len(SCREEN[0])):
            if SCREEN[j][i] == True:
                count += 1

print count

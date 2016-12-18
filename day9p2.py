import sys

def decompress_line(line):
    if "(" not in line:
        # print "not in", line
        return len(line), 1

    # There's at least one (marker).
    length = 0
    in_marker = False
    collecting_rep = False
    marker = ""
    rep = ""
    nchars = 0
    nreps = 0

    for char in line:
        if collecting_rep:
            rep += char
            nchars -= 1
            if nchars == 0:
                collecting_rep = False
                # print "rep", rep
                sub_nchars, sub_nreps = decompress_line(rep)
                length += sub_nchars * sub_nreps * nreps
                nreps = 0
                rep = ""
            continue

        if in_marker:
            # Markers don't count for length.
            if char == ")":
                in_marker = False
                nchars, nreps = marker.split("x")
                nchars = int(nchars)
                nreps = int(nreps)
                collecting_rep = True
            else:
                marker += char

        elif not in_marker:
            if char == "(":
                in_marker = True
                marker = ""
            else:
                length += 1

    assert(nchars == 0)
    return length, 1


length = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        line = line.strip()
        # print line
        l, reps = decompress_line(line)
        print l * reps
        print

import sys

length = 0

with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        line = line.strip()
        decompressed_line = ""

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
                    decompressed_line += rep * nreps
                    rep = ""
                    nreps = 0
                continue

            if in_marker:
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
                    decompressed_line += char

        # print decompressed_line, len(decompressed_line)
        length += len(decompressed_line)

print length

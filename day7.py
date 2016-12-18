import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        line = line.strip()
        seen = []

        abba = ""
        tls = False
        hypernet = False
        abba_in_hypernet = False
        for char in line:
            if char == "[":
                hypernet = True
                seen = []
                continue
            if char == "]":
                hypernet = False
                seen = []
                continue

            if len(seen) == 0 or (len(seen) == 1 and char != seen[0]):
                seen.append(char)
            elif len(seen) == 2:
                if seen[1] != char:
                    seen = seen[1:]
                seen.append(char)
            elif len(seen) == 3:
                if seen[0] == char:
                    abba = "".join(seen) + char
                    if hypernet:
                        tls = False
                        abba_in_hypernet = True
                        break
                    else:
                        tls = True
                    abba = "".join(seen) + char
                else:
                    seen = seen[2:]
                    seen.append(char)

            # print seen, char

        if tls:
            print "TLS", abba, line
            count += 1
        elif abba_in_hypernet:
            print "ABBA in hypernet", abba, line

print count

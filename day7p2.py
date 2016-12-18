import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        line = line.strip()
        curr = []
        abas = set([])
        babs = set([])

        ssl = False
        hypernet = False
        abba_in_hypernet = False
        for char in line:
            if char == "[":
                hypernet = True
                curr = []
                continue
            if char == "]":
                hypernet = False
                curr = []
                continue

            if len(curr) == 0:
                curr.append(char)
            if  len(curr) == 1:
                if char != curr[0]:
                    curr.append(char)
                else:
                    curr = [char]
            elif len(curr) == 2:
                if char == curr[0] and char != curr[1]:
                    curr.append(char)
                    if hypernet:
                        babs.add("".join(curr))
                    else:
                        abas.add("".join(curr))
                    curr = curr[1:]
                elif char != curr[0]:
                    if char != curr[1]:
                        curr = curr[1:] + [char]
                    else:
                        curr = [char]

        # if tls:
        #     print "TLS", abba, line
        #     count += 1
        # elif abba_in_hypernet:
        #     print "ABBA in hypernet", abba, line

        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if bab in babs:
                print "ABA"
                print aba, babs
                print line
                print
                count += 1
                break

print count



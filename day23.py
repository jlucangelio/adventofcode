import sys

def print_regs(regs):
    print "A:%d B:%d C:%d D:%d" % (regs["a"],regs["b"],regs["c"],regs["d"])


regs = {
    "a": 12,
    "b": 0,
    "c": 0,
    "d": 0
}

regs["a"] = int(sys.argv[2])

pc = 0
instructions = []

steps = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()

    instructions = [line.strip().split() for line in lines]
    toggled = [False for line in lines]

    while pc < len(instructions):
        if steps % 1000000 == 0:
            print steps / 1000000

        tokens = instructions[pc]
        op = tokens[0]
        is_toggled = toggled[pc]

        # print_regs(regs)
        # print pc, " ".join(tokens), is_toggled

        if (is_toggled and op == "jnz") or (not is_toggled and op == "cpy"):
            # print "will do cpy"
            src = tokens[1]
            dst = tokens[2]

            if dst in regs:
                if src in regs:
                    regs[dst] = regs[src]
                else:
                    regs[dst] = int(src)

            offset = 1

        elif (is_toggled and (op == "dec" or op == "tgl")) or (not is_toggled and op == "inc"):
            # print "will do inc"
            dst = tokens[1]
            if dst in regs:
                regs[dst] += 1
            offset = 1

        elif (is_toggled and op == "inc") or (not is_toggled and op == "dec"):
            # print "will do dec"
            dst = tokens[1]
            if dst in regs:
                regs[dst] -= 1
            offset = 1

        elif (is_toggled and op == "cpy") or (not is_toggled and op == "jnz"):
            # print "will do jnz"
            val = tokens[1]
            jnz_offset_src = tokens[2]
            if jnz_offset_src in regs:
                offset = regs[jnz_offset_src]
            else:
                offset = int(jnz_offset_src)

            if val in regs:
                if regs[val] == 0:
                    offset = 1
            elif int(val) == 0:
                offset = 1

        elif (not is_toggled and op == "tgl"):
            # print "will do tgl"
            tgl_src = tokens[1]
            if tgl_src in regs:
                tgl_offset = regs[tgl_src]
            else:
                tgl_offset = int(tgl_src)

            if pc + tgl_offset < len(toggled):
                toggled[pc + tgl_offset] = True

        pc += offset
        steps += 1
        # print

print regs["a"]

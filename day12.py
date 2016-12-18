import sys

def print_regs(regs):
    print "A:%d B:%d C:%d D:%d" % (regs["a"],regs["b"],regs["c"],regs["d"])


regs = {
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0
}

pc = 0

instructions = []

steps = 0

with open(sys.argv[1]) as f:
    lines = f.readlines()

    instructions = [line.strip().split() for line in lines]
    while pc < len(instructions):
        tokens = instructions[pc]
        op = tokens[0]

        # print_regs(regs)
        # print pc, " ".join(tokens)

        if op == "cpy":
            src = tokens[1]
            dst = tokens[2]

            if src in regs:
                regs[dst] = regs[src]
            else:
                regs[dst] = int(src)

            offset = 1

        elif op == "inc":
            regs[tokens[1]] += 1
            offset = 1

        elif op == "dec":
            regs[tokens[1]] -= 1
            offset = 1

        elif op == "jnz":
            val = tokens[1]
            offset = int(tokens[2])

            if val in regs:
                if regs[val] == 0:
                    offset = 1
            elif int(val) == 0:
                offset = 1

        pc += offset
        steps += 1

print regs["a"]

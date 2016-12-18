import sys

class Bot(object):
    def __init__(self, num, low, high):
        self.num = num
        self.high = high
        self.low = low
        self.values = []

    def receive(self, value, bots):
        if len(self.values) >= 2:
            assert("bot already has two values")
        self.values.append(value)
        if len(self.values) == 2:
            if 17 in self.values and 61 in self.values:
                print "is bot %d" % self.num
            self.give(bots)

    def give(self, bots):
        if self.low in bots:
            bots[self.low].receive(min(self.values), bots)
        else:
            self.low.receive(min(self.values))
        if self.high in bots:
            bots[self.high].receive(max(self.values), bots)
        else:
            self.high.receive(max(self.values))

class Output(object):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return "output %d" % num

    def receive(self, value):
        print "output %d got value %d" % (self.num, value)


bots = {}
values = {}
outputs = {}

with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        line = line.strip()

        tokens = line.split()
        if tokens[0] == "bot":
            botnum = int(tokens[1])
            tok_low = int(tokens[6])
            tok_high = int(tokens[11])

            if tokens[5] == "output":
                low = Output(tok_low)
                outputs[tok_low] = low
            else:
                low = tok_low

            if tokens[10] == "output":
                high = Output(tok_high)
                outputs[tok_high] = high
            else:
                high = tok_high

            bots[botnum] = Bot(botnum, low, high)

        elif tokens[0] == "value":
            values[int(tokens[1])] = int(tokens[5])

print values
print outputs

for value, bot in values.iteritems():
    bots[bot].receive(value, bots)
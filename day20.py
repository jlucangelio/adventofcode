import sys

from collections import namedtuple

Interval = namedtuple("Interval", "b e")


def contains(self, other):
    return other.b >= self.b and other.e <= self.e


class IntervalNode(object):
    def __init__(self, interval):
        self.ival = interval

        self.left = None
        self.right = None

        self.max = interval.e


    def insert(self, interval):
        # print self.ival, interval
        if interval.b < self.ival.b:
            if self.left is None:
                self.left = IntervalNode(interval)
            else:
                self.left.insert(interval)

        else:
            if self.right is None:
                self.right = IntervalNode(interval)
            else:
                self.right.insert(interval)

        if interval.e > self.max:
            self.max = interval.e


    def search(self, value):
        if value > self.max:
            # print "value", value, "bigger than max", self.max
            return False

        if value >= self.ival.b and value <= self.ival.e:
            # print "in range", self.ival
            return True

        if self.left is not None:
            # print "to left"
            in_left = self.left.search(value)
            if in_left:
                # print "to left true"
                return True

        if value >= self.ival.b:
            if self.right is not None:
                # print "to right"
                in_right = self.right.search(value)
                if in_right:
                    # print "to right true"
                    return True

        # print "nothing"
        return False


    def search_ival(self, interval):
        if contains(self.ival, interval):
            return True

        if self.left is not None and self.left.search_ival(interval):
            return True

        if interval.b >= self.ival.b:
            if self.right is not None and self.right.search_ival(interval):
                return True

        return False


node = None
with open(sys.argv[1]) as f:
    lines = f.readlines()

    for line in lines:
        b, e = line.strip().split("-")
        ival = Interval(int(b), int(e))

        if node is None:
            node = IntervalNode(ival)
        else:
            # print "inserting", ival
            node.insert(ival)

addr = 0
count = 0
while addr < 2**32:
    # if addr % 1000000 == 0:
    #     print addr

    if node.search(addr) is False:
        print addr
        addr += 1
        count += 1
        continue

    if node.search_ival(Interval(addr, addr + 10000)):
        addr += 10000
    else:
        addr += 1

print "count", count

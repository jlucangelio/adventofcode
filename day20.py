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
            return None

        if value >= self.ival.b and value <= self.ival.e:
            # print "in range", self.ival
            return self.ival.e

        if self.left is not None:
            # print "to left"
            in_left = self.left.search(value)
            if in_left is not None:
                # print "to left true"
                return in_left

        if value >= self.ival.b:
            if self.right is not None:
                # print "to right"
                in_right = self.right.search(value)
                if in_right is not None:
                    # print "to right true"
                    return in_right

        # print "nothing"
        return None


    def search_ival(self, interval):
        if contains(self.ival, interval):
            return self.ival.e

        if self.left is not None:
            left_ival = self.left.search_ival(interval)
            if left_ival is not None:
                return left_ival.e

        if interval.b >= self.ival.b:
            if self.right is not None:
                right_ival = self.right.search_ival(interval)
                if right_ival is not None:
                    return right_ival.e

        return None


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

    e = node.search(addr)
    if e is None:
        print addr
        addr += 1
        count += 1
        continue
    else:
        addr = e + 1

print "count", count

import hashlib

from collections import namedtuple

Position = namedtuple("Position", "x y")

INPUT = "qljzarfv"

DIRECTIONS = {
    0: "U",
    1: "D",
    2: "L",
    3: "R",
}

def hash_path(path):
    h = hashlib.md5(INPUT + path).hexdigest()
    return h[:4]


def is_door_open(c):
    return c in "bcdef"


def compute_doors(h):
    return dict([(DIRECTIONS[i], is_door_open(h[i])) for i in range(4)])


best_path = None

def find_path(curr_pos, path, longest=False):
    global best_path

    if curr_pos.x == 3 and curr_pos.y == 3:
        if best_path is None:
            best_path = path
        elif longest == False and len(path) < len(best_path):
            best_path = path
        elif longest == True and len(path) > len(best_path):
            best_path = path
        return

    if longest == False and best_path is not None and len(path) > len(best_path):
        return

    h = hash_path(path)
    doors = compute_doors(h)

    for direction in doors:
        door_open = doors[direction]
        if direction == "U":
            if curr_pos.x > 0 and door_open:
                find_path(Position(curr_pos.x - 1, curr_pos.y), path + direction, longest)

        elif direction == "D":
            if curr_pos.x < 3 and door_open:
                find_path(Position(curr_pos.x + 1, curr_pos.y), path + direction, longest)

        if direction == "L":
            if curr_pos.y > 0 and door_open:
                find_path(Position(curr_pos.x, curr_pos.y - 1), path + direction, longest)

        elif direction == "R":
            if curr_pos.y < 3 and door_open:
                find_path(Position(curr_pos.x, curr_pos.y + 1), path + direction, longest)


find_path(Position(0, 0), "")
print "best path", best_path
print

best_path = None
find_path(Position(0, 0), "", longest=True)
print "best path", best_path, len(best_path)

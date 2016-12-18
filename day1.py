from collections import namedtuple

INPUT = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"
# INPUT = "L2, L3"

TURN = {
    "N": {
        "L": "W",
        "R": "E"
    },
    "E": {
        "L": "N",
        "R": "S"
    },
    "S": {
        "L": "E",
        "R": "W"
    },
    "W": {
        "L": "S",
        "R": "N"
    }
}

HORIZONTAL = 0
VERTICAL = 1


def turn(heading, direction):
    return TURN[heading][direction]


def walk(location, axis, direction, blocks, visited):
    for _ in range(blocks):
        location[axis] += direction
        if tuple(location) in visited:
            print distance(location)
        visited.add(tuple(location))

    return location


def move(location, heading, blocks, visited):
    if heading == "N":
        location = walk(location, VERTICAL, 1, blocks, visited)
    if heading == "S":
        location = walk(location, VERTICAL, -1, blocks, visited)

    if heading == "E":
        location = walk(location, HORIZONTAL, 1, blocks, visited)
    if heading == "W":
        location = walk(location, HORIZONTAL, -1, blocks, visited)

    return location


def distance(location):
    return abs(location[HORIZONTAL]) + abs(location[VERTICAL])


def main(turns):
    location = [0, 0]
    heading = "N"
    visited = set([])

    for movement in turns.split(", "):
        direction = movement[0]
        blocks = int(movement[1:])

        heading = turn(heading, direction)
        location = move(location, heading, blocks, visited)

    return distance(location)

if __name__ == "__main__":
    print main(INPUT)

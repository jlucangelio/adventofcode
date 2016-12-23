from copy import copy

# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# F4
# F3 CoC CuC RuC PtC
# F2 CoG CuG RuG PtG
# F1 PrG PrC

# F4 .  .  .  .  .
# F3 .  .  .  LG .
# F2 .  HG .  .  .
# F1 E  .  HM .  LM


# def make_state(f1, f2, f3, f4):
#     return (f1, f2, f3, f4)

def make_state(floor_num, new_floors, all_floors):
    final_floors = []
    for i, floor in enumerate(all_floors):
        if i in new_floors:
            final_floors.append(frozenset(new_floors[i]))
        else:
            final_floors.append(floor)

    return (floor_num, tuple(final_floors))


def is_valid(state):
    valid = True
    floors = state[1]
    for parts in floors:
        seen_parts = set()
        for part_i in parts:
            for part_j in parts:
                if part_i == part_j:
                    continue

                type_i = part_i[0]
                type_j = part_j[0]
                if type_i != type_j and part_i[1:] != part_j[1:]:
                    # incompatible chip and gen. find corresponding gen:

                    if type_i == "m":
                        if ("g" + part_i[1:]) not in parts:
                            return False

                    elif type_j == "m":
                        if ("g" + part_j[1:]) not in parts:
                            return False

    return valid


def is_target(state):
    return TARGET[1][3] == state[1][3]


def found(state_set):
    for state in state_set:
        if state[0] != 3:
            continue

        if TARGET[1][3] == state[1][3]:
            return True

    return False


def to_state(s):
    n, floorstr = s.split(":")
    floors = []
    for floor in floorstr.split("|"):
        if len(floor) > 0:
            floors.append(frozenset(floor.split(",")))
        else:
            floors.append(frozenset())

    return (int(n), tuple(floors))


def to_string(state):
    return "%d:%s" % (state[0], "|".join([",".join(floor) for floor in state[1]]))


print is_valid(to_state("1:|gh,ml|gl,mh|"))
print is_valid(to_state("2:|gpt,gru,mpr,gpr,gco|mco,mru,mcu,gcu,mpt|"))

print "1:|gh,ml|gl,mh|"
print to_string(to_state("1:|gh,ml|gl,mh|"))

# F4
# F3 CoC CuC RuC PtC
# F2 CoG CuG RuG PtG
# F1 PrG PrC

TARGET = to_state("3:|||mh,ml,gh,gl")
initial = to_state("0:mh,ml|gh|gl|")

TARGET = to_state("3:|||mpr,mru,mpt,mcu,mco,gpr,gru,gpt,gcu,gco,me,ge,md,gd")
# TARGET = to_state("3:|||mpr,mru,mpt,mcu,mco,gpr,gru,gpt,gcu,gco")
initial = to_state("0:mpr,gpr,me,ge,md,gd|gco,gcu,gru,gpt|mco,mcu,mru,mpt|")
# initial = to_state("0:mpr,gpr|gco,gcu,gru,gpt|mco,mcu,mru,mpt|")

LEVELS = 100

level = 0
prev_set = set()
current_set = set([initial])
next_set = set()
was_found = False

for i in range(LEVELS):
    print i, len(current_set)
    # print [to_string(state) for state in current_set]
    if was_found:
        break

    for state in current_set:
        if was_found:
            break

        if not is_valid(state):
            continue

        floor_num, floors = state

        if len(floors[floor_num]) == 0:
            continue

        parts = floors[floor_num]
        floor_below = None
        floor_above = None
        for i, part in enumerate(parts):
            if floor_num > 0:
                floor_below = set(floors[floor_num - 1])
                floor_below.add(part)
                curr_floor = set(parts)
                curr_floor.remove(part)
                new_state = make_state(floor_num - 1, {floor_num: curr_floor, (floor_num - 1):floor_below}, floors)
                if is_valid(new_state):
                    if is_target(new_state):
                        print "FOUND", level + 1
                        print new_state
                        was_found = True
                        break

                    if new_state not in prev_set:
                        next_set.add(new_state)

            if floor_num < 3:
                floor_above = set(floors[floor_num + 1])
                floor_above.add(part)
                curr_floor = set(parts)
                curr_floor.remove(part)
                new_state = make_state(floor_num + 1, {floor_num: curr_floor, (floor_num + 1):floor_above}, floors)
                if is_valid(new_state):
                    if is_target(new_state):
                        print "FOUND", level + 1
                        print new_state
                        was_found = True
                        break

                    if new_state not in prev_set:
                        next_set.add(new_state)

        seen_parts = set()
        for part_i in parts:
            for part_j in parts:
                if part_i == part_j:
                    continue

                if (part_j, part_i) in seen_parts:
                    continue

                if part_i[0] != part_j[0] and part_i[1:] != part_j[1:]:
                    # incompatible chip and gen.
                    seen_parts.add((part_i, part_j))
                    continue

                # print part_i, part_j

                if floor_num > 0:
                    floor_below = set(floors[floor_num - 1])
                    floor_below.add(part_i)
                    floor_below.add(part_j)
                    curr_floor = set(parts)
                    curr_floor.remove(part_i)
                    curr_floor.remove(part_j)
                    new_state = make_state(floor_num - 1, {floor_num: curr_floor, (floor_num - 1):floor_below}, floors)
                    if is_valid(new_state):
                        if is_target(new_state):
                            print "FOUND", level + 1
                            print new_state
                            was_found = True
                            break

                        if new_state not in prev_set:
                            next_set.add(new_state)

                if floor_num < 3:
                    floor_above = set(floors[floor_num + 1])
                    floor_above.add(part_i)
                    floor_above.add(part_j)
                    curr_floor = set(parts)
                    curr_floor.remove(part_i)
                    curr_floor.remove(part_j)
                    new_state = make_state(floor_num + 1, {floor_num: curr_floor, (floor_num + 1):floor_above}, floors)
                    if is_valid(new_state):
                        if is_target(new_state):
                            print "FOUND", level + 1
                            print new_state
                            was_found = True
                            break

                        if new_state not in prev_set:
                            next_set.add(new_state)

                seen_parts.add((part_i, part_j))

    level += 1

    # if next_set == current_set:
    #     break

    prev_set = copy(current_set)
    current_set = copy(next_set)
    next_set = set()
    # all_set.update(next_set)

# for state in current_set:
#     if state[0] == "3":
#         print state

# print current_set
# print len(all_set)

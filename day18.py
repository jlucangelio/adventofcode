STARTING_ROW = [c == "^" for c in ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."]
# STARTING_ROW = [c == "^" for c in ".^^.^.^^^^"]

current_row = STARTING_ROW
count = sum([1 for e in current_row if not e])
next_row = [None for _ in range(len(STARTING_ROW))]

# for _ in range(40):
for _ in range(400000 - 1):
    for i in range(len(next_row)):
        if i == 0:
            left = False
        else:
            left = current_row[i-1]

        center = current_row[i]

        if i == len(STARTING_ROW) - 1:
            right = False
        else:
            right = current_row[i+1]

        next_row[i] = (left and center and not right) or (center and right and not left) or (left and not center and not right) or (right and not left and not center)

    current_row = next_row
    count += sum([1 for e in current_row if not e])
    next_row = [None for _ in range(len(STARTING_ROW))]

print count

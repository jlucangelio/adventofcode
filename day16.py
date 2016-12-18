from copy import copy

# Call the data you have at this point "a".
# Make a copy of "a"; call this copy "b".
# Reverse the order of the characters in "b".
# In "b", replace all instances of 0 with 1 and all 1s with 0.
# The resulting data is "a", then a single 0, then "b".

def dragon_one(data):
    new_data = copy(data)
    new_data.reverse()

    new_data = [(digit + 1) % 2 for digit in new_data]
    return data + [0] + new_data


# Consider each pair: 11, 00, 10, 11, 01, 00.
# These are same, same, different, same, different, same, producing 110101.
# The resulting string has length 6, which is even, so we repeat the process.
# The pairs are 11 (same), 01 (different), 01 (different).
# This produces the checksum 100, which has an odd length, so we stop.

def calculate_checksum(data):
    if len(data) % 2 == 1:
        return data

    checksum = []

    for i in range(len(data) // 2):
        pair = data[2*i:2*i+2]
        if pair[0] == pair[1]:
            checksum.append(1)
        else:
            checksum.append(0)

    return calculate_checksum(checksum)

def to_list(s):
    return [int(c) for c in s]


print calculate_checksum(to_list("110010110100"))

data = to_list("00101000101111010")

while len(data) < 35651584:
    data = dragon_one(data)

# print data
print "".join([str(digit) for digit in calculate_checksum(data[:35651584])])

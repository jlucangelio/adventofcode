def is_real(name, checksum):
    frequencies = {}

    for letter in name:
        if letter not in frequencies:
            frequencies[letter] = 1
            continue
        frequencies[letter] += 1

    sorted_letters = sorted(frequencies.keys(), key=lambda k: (frequencies[k], ord("z") - ord(k)), reverse=True)
    return checksum in "".join(sorted_letters)


def rotate(name, sector_id):
    decrypted_name = ""
    for token in name.split("-"):
        for letter in token:
            decrypted_name += chr((ord(letter) - ord("a") + int(sector_id)) % 26 + ord("a"))
        decrypted_name += " "

    print decrypted_name, sector_id


s = 0
with open("day4.input") as f:
    lines = f.readlines()

    for line in lines:
        tokens = line.strip().split("-")
        name = "".join(tokens[:-1])
        sector_id, checksum = tokens[-1].split("[")
        checksum = checksum[:-1]

        if is_real(name, checksum):
            s += int(sector_id)
            rotate(name, sector_id)
        # print name, sector_id, checksum

print s

import hashlib

SEED = "yjdafjpo"
# SEED = "abc"

# hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

def all_equal(str):
    return all([c == str[0] for c in str])

def repeat_hash(s):
    h = hashlib.md5(s).hexdigest()

    for _ in range(2016):
        h = hashlib.md5(h).hexdigest()

    return h


hashes = {}

index = 0
triplets = {}

quintets = {}

keys = {}

while len(keys) < 64:
    if index % 1000 == 0:
        print "at index %d" % index

    if index in hashes:
        h = hashes[index]
    else:
        message = SEED + str(index)
        h = repeat_hash(message)

    for i, char in enumerate(h):
        if i < 2:
            continue

        possible_run = h[i-2:i+1]

        if all_equal(possible_run):
            first_triplet = possible_run

            if first_triplet in quintets:
                for qindex in quintets[first_triplet]:
                    if qindex > index and qindex - index <= 1000:
                        print index, first_triplet, qindex
                        keys[index] = first_triplet
                        break

            if index not in keys:
                for qindex in range(index + 1, index + 1001):
                    if qindex in hashes:
                        newh = hashes[qindex]
                    else:
                        newmessage = SEED + str(qindex)
                        newh = repeat_hash(newmessage)

                    for i, char in enumerate(newh):
                        if i < 4:
                            continue

                        possible_run = newh[i-4:i+1]

                        # if all_equal(possible_run):
                        #     prefix = possible_run[:3]
                        #     if prefix in quintets:
                        #         quintets[prefix].add(qindex)
                        #     else:
                        #         quintets[prefix] = set([qindex])

                        if possible_run[0] != first_triplet[0]:
                            continue

                        if all_equal(possible_run):
                            quintet = possible_run
                            print index, first_triplet, qindex, quintet
                            keys[index] = first_triplet

                            if first_triplet in quintets:
                                quintets[first_triplet].add(qindex)
                            else:
                                quintets[first_triplet] = set([qindex])

                            break

            # only consider first triplet
            break

    index += 1

print "final index", index - 1

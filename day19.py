# NELVES = 5
NELVES = 3012210

class LLNode(object):
    def __init__(self, v, p, n):
        self.value = v
        self.prevn = p
        self.nextn = n


    def insert(self, v):
        new = LLNode(v, self, self.nextn)
        self.nextn = new
        return new


    def remove(self):
        n = self.nextn
        self.prevn.nextn = n
        n.prevn = self.prevn
        return self


    def __str__(self):
        return "v: %s, p: %r, n: %r" % (self.value, self.prevn, self.nextn)


def print_list(head, l):
    node = head
    count = 0
    while node is not None and count < l:
        print node
        node = node.nextn
        count += 1


elves_with_presents = set([i for i in range(NELVES)])
presents = [1 for _ in range(NELVES)]
stealing = False
elf_stealing = None

while len(elves_with_presents) > 1:
    print len(elves_with_presents)
    for index in range(len(presents)):
        if not stealing:
            if presents[index] > 0:
                stealing = True
                elf_stealing = index
        elif stealing:
            if presents[index] > 0:
                # if index == elf_stealing:
                #     break
                presents[elf_stealing] += presents[index]
                presents[index] = 0
                stealing = False
                elf_stealing = None
                elves_with_presents.remove(index)

for elf in elves_with_presents:
    print elf + 1
print


head = LLNode(1, None, None)
node = head
val_to_node = {}

for i in range(1, NELVES):
    node = node.insert(i + 1)
    val_to_node[i + 1] = node

node.nextn = head
head.prevn = val_to_node[NELVES]
node_count = NELVES

val_across = None
if NELVES % 2 == 0:
    val_across = (1 + NELVES / 2) % NELVES
else:
    val_across = (1 + (NELVES - 1) / 2) % NELVES

node = head
across = val_to_node[val_across]
while node_count > 1:
    if node_count % 100000 == 0:
        print node_count
    removed = across.remove()
    node = node.nextn
    across = removed.nextn
    if node_count % 2 == 1:
        across = across.nextn

    node_count -= 1

print node

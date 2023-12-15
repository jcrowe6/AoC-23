steps = []
with open("input.txt") as f:
    line = f.readline()
    steps = line[:-1].split(',')

print(steps)
print(len(steps))

def hash(str):
    curr = 0
    for c in str:
        curr += ord(c)
        curr = curr*17
        curr = curr % 256
    return curr

total = sum(map(hash, steps))
print(total)
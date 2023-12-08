import math

dirs = ""
edges = {}
currnodes = []

with open("input.txt") as f:
    dirs = f.readline()[:-1]
    f.readline()
    while True:
        line = f.readline()
        if line == '': break
        node = line[0:3]
        l = line[7:10]
        r = line[12:15]
        if node[2] == 'A': currnodes.append(node)
        edges[node] = (line[7:10], line[12:15])

def step_all(dir):
    for i in range(len(currnodes)):
        node = currnodes[i]
        if dir == 'L':
            currnodes[i] = edges[node][0]
        else:
            currnodes[i] = edges[node][1]

def all_end_z():
    for node in currnodes:
        if node[2] != 'Z':
            return False
    return True

def steps_to_all_z():
    steps = 0
    while True:
        for dir in dirs:
            step_all(dir)
            steps += 1
            if all_end_z():
                return steps
            if steps%10000000 == 0:
                print(steps)

# too slow!

# this iterates, beginning with start node, until n 'Z's have been reached. Returns a list of (XXZ, steps) tuples
def steps_to_n_zs(start, n):
    curr = start
    steps = 0
    zs = []
    while True:
        for dir in dirs:
            if dir == 'L':
                curr = edges[curr][0]
            else: # R
                curr = edges[curr][1]
            steps += 1
            if curr[2] == 'Z':
                zs.append((curr, steps))
                if len(zs) == n:
                    return zs

'''for start in currnodes:
    zs = steps_to_n_zs(start,10)
    print(zs)
    for a,b in zip(zs,zs[1:]):
        print(b[1]-a[1], end = ' ')
    print()'''

#so, each start node hits its own specific XXZ node repeatedly...
# and at the same regular interval

freqs = []
for start in currnodes:
    zs = steps_to_n_zs(start,2)
    freqs.append(zs[1][1]-zs[0][1])
print(freqs)

# I think the answer is the LCM of these
lcm = freqs[0]
for f in freqs[1:]:
    lcm = math.lcm(lcm, f)
print(lcm)
dirs = ""
edges = {}

with open("input.txt") as f:
    dirs = f.readline()[:-1]
    print(dirs)
    f.readline()
    while True:
        line = f.readline()
        if line == '': break
        edges[line[0:3]] = (line[7:10], line[12:15])
    print(edges)

def steps_to_zzz():
    curr = "AAA"
    steps = 0
    while True:
        for dir in dirs:
            if dir == 'L':
                curr = edges[curr][0]
            else: # R
                curr = edges[curr][1]
            steps += 1
            if curr == "ZZZ":
                return steps

print(steps_to_zzz())
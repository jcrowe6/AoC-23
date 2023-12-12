problems = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        spring,nums = line.split(' ')
        spring = list(spring)
        nums = list(map(int,nums.split(',')))
        problems.append((spring,nums))

# kinda a search problem?
# idea 1: recursively explore all spring placements

def groups_match_target(row, target):
    spring_ct = 0
    actual = []
    for c in row:
        if c == '?':
            print("error: called on unfinished row")
        elif c == '#':
            spring_ct += 1
        else:
            if spring_ct > 0:
                actual.append(spring_ct)
                spring_ct = 0
    if spring_ct > 0: actual.append(spring_ct)
    return actual == target

def explore(row, i, target):
    if i >= len(row):
        return 1 if groups_match_target(row,target) else 0
    chr = row[i]
    if chr == '?':
        row[i] = '.'
        blank = explore(row,i+1,target)
        row[i] = '#'
        spring = explore(row,i+1,target)
        row[i] = '?'
        return blank+spring
    else:
        return explore(row,i+1,target)

total = 0
for row,target in problems:
    total += explore(row,0,target)
print(total)
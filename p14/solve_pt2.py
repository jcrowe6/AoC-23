rocks = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        rocks.append(list(line[:-1]))

# idea: iterate over array, moving movable rocks one unit, until it converges
def move_dir(i,j, dir):
    c = rocks[i][j]
    if c == 'O':
        if dir == 'N':
            newi,newj = i-1,j
        elif dir == 'E':
            newi,newj = i,j+1
        elif dir == 'S':
            newi,newj = i+1,j
        else:
            newi,newj = i,j-1
        if newi >= 0 and newi < len(rocks) and newj >= 0 and newj < len(rocks[0]):
            if rocks[newi][newj] == '.':
                rocks[newi][newj] = 'O'
                rocks[i][j] = '.'
                return True
    return False

def converge_dir(dir):
    while True:
        something_moved = False
        for i in range(len(rocks)):
            for j in range(len(rocks[0])):
                if move_dir(i,j,dir):
                    something_moved = True
        if not something_moved:
            break
    

def cycle():
    converge_dir('N')
    converge_dir('W')
    converge_dir('S')
    converge_dir('E')



totals = {}
max_ = 1000
for i in range(max_):
    cycle()

    if max_-i < 400:
        weight = len(rocks)
        total = 0
        for row in rocks:
            for c in row:
                if c == 'O':
                    total += weight
            weight -= 1
        if total not in totals:
            totals[total] = [i+1]
        else:
            totals[total].append(i+1)

print(totals)
amt = len(totals)
print(amt)
for k in totals:
    v = totals[k]
    totals[k] = list(map(lambda x: x % 51, v))
print(totals)
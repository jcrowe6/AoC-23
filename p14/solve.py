rocks = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        rocks.append(list(line[:-1]))

# idea: iterate over array, moving movable rocks one unit, until it converges
def move_pos(i,j):
    c = rocks[i][j]
    if c == 'O' and i > 0 and rocks[i-1][j] == '.': # round boulder can move
        rocks[i][j] = '.'
        rocks[i-1][j] = 'O'
        return True
    return False

while True:
    something_moved = False
    for i in range(len(rocks)):
        for j in range(len(rocks[0])):
            if move_pos(i,j):
                something_moved = True
    if not something_moved:
        break

weight = len(rocks)
total = 0
for row in rocks:
    for c in row:
        if c == 'O':
            total += weight
    weight -= 1

print(total)
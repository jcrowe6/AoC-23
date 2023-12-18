cave = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        cave.append(list(line[:-1]))

def in_bounds(r,c):
    return r >= 0 and r < len(cave) and c >= 0 and c < len(cave[0])


# logic for computing next cells of the beam with splitting andboundary logic
def next_cells(r,c,dir):
    cell = cave[r][c]
    if cell == '.':
        if dir == 'R':
            if in_bounds(r,c+1):
                return [(r,c+1,'R')]
        if dir == 'D':
            if in_bounds(r+1,c):
                return [(r+1,c,'D')]
        if dir == 'L':
            if in_bounds(r,c-1):
                return [(r,c-1,'L')]
        if dir == 'U':
            if in_bounds(r-1,c):
                return [(r-1,c,'U')]
    if cell == '\\':
        if dir == 'R':
            if in_bounds(r+1,c):
                return [(r+1,c,'D')]
        if dir == 'D':
            if in_bounds(r,c+1):
                return [(r,c+1,'R')]
        if dir == 'L':
            if in_bounds(r-1,c):
                return [(r-1,c,'U')]
        if dir == 'U':
            if in_bounds(r,c-1):
                return [(r,c-1,'L')]
    if cell == '/':
        if dir == 'R':
            if in_bounds(r-1,c):
                return [(r-1,c,'U')]
        if dir == 'D':
            if in_bounds(r,c-1):
                return [(r,c-1,'L')]
        if dir == 'L':
            if in_bounds(r+1,c):
                return [(r+1,c,'D')]
        if dir == 'U':
            if in_bounds(r,c+1):
                return [(r,c+1,'R')] 
    if cell == '-':
        if dir == 'R':
            if in_bounds(r,c+1):
                return [(r,c+1,'R')]
        if dir == 'D' or dir == 'U':
            # split!
            out = []
            if in_bounds(r,c-1):
                out.append((r,c-1,'L'))
            if in_bounds(r,c+1):
                out.append((r,c+1,'R'))
            return out
        if dir == 'L':
            if in_bounds(r,c-1):
                return [(r,c-1,'L')]
    if cell == '|':
        if dir == 'R' or dir == 'L':
            out = []
            if in_bounds(r-1,c):
                out.append((r-1,c,'U'))
            if in_bounds(r+1,c):
                out.append((r+1,c,'D'))
            return out
        if dir == 'U':
            if in_bounds(r-1,c):
                return [(r-1,c,'U')]
        if dir == 'D':
            if in_bounds(r+1,c):
                return [(r+1,c,'D')]
    return []
              

        

frontier = [(0,0,'R')]
explored = set()
energized = set()
while len(frontier) > 0:
    r,c,dir = frontier.pop(0)
    if (r,c) not in energized:
        energized.add((r,c))
    if (r,c,dir) not in explored:
        explored.add((r,c,dir))
        nexts = next_cells(r,c,dir)
        for c in nexts:
            frontier.append(c)
        
    #print(r,c,dir)
    print(len(explored))
print(len(energized))

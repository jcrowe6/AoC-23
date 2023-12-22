import numpy as np
import heapq
city = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        city.append(list(map(int,line[:-1])))
city = np.array(city)
goal = (city.shape[0]-1,city.shape[1]-1)
dist = {(0,0,'S',1):0} # dist[(a,b,c)] is dist of shortest path from source to (a,b) while moving c steps in a straight line previously
prev = {}
visited = set()

def smallest_unvisited():
    min_ = None
    argmin = None
    for k in dist:
        if k not in visited and (min_ is None or dist[k] < min_):
            min_ = dist[k]
            argmin = k
    return argmin

def prev2(row,col):
    out = []
    for i in range(2):
        if (row,col) in prev:
            out.append(prev[(row,col)])
            row,col = prev[row,col]
    return out

# given a current position, returns a coordinate that cannot be considered to move to if it would create a series of 4+ squares in a line
# if this is not the case, returns (-1,-1)
def unavailable_space(row,col):
    prevs = prev2(row,col)
    if len(prevs) < 2: return (-1, -1) # not enough previous spaces 
    last,secnd = prevs
    lr,lc = last
    sr,sc = secnd
    # "in a row" means all 3 of one coordinate is the same.
    if row == lr and lr == sr: 
        if col > lc: return (row,col+1)
        else: return (row,col-1)
    elif col == lc and lc == sc:
        if row > lr: return (row+1,col)
        else: return (row-1,col)
    else:
        return (-1,-1)
# turns out, restricting the "neighbors" available to nodes like on the fly is wrong. 
# because, it will mark nodes as visited that were visited by a specific (possibly not optimal) path
# and later wiggly paths that took more turns to be adjacent that node will not consider it even if they have better heat loss
# need to restructure the information I'm keeping instead / make the graph bigger

# given current row, column, direction of travel, and number of steps in that direction of travel,
# returns legal neighbors
def neighbors(row,col,dir,steps):
    out = []
    if dir == 'S':
        out = [(0,1,'R',2),(1,0,'D',2)]
    else:
        for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
            if (dir == 'U' and r>row) or (dir == 'R' and c<col) or (dir == 'D' and r<row) or (dir == 'L' and c>col): continue
            if r >= 0 and r < len(city) and c >= 0 and c < len(city[0]):
                if r>row: # downward
                    if dir == 'L' or dir == 'R': out.append((r,c,'D',2))
                    # must be already moving D. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'D',3))
                if r<row: # upward
                    if dir == 'L' or dir == 'R': out.append((r,c,'U',2))
                    # must be already moving U. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'U',3))
                if c>col: # rightward
                    if dir == 'U' or dir == 'D': out.append((r,c,'R',2))
                    # must be already moving R. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'R',3))
                if c<col: # leftward
                    if dir == 'U' or dir == 'D': out.append((r,c,'L',2))
                    # must be already moving L. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'L',3))
    #print(row,col,dir,steps)
    #print(out)
    #input()
    return out

# dijiktra's
while True:
    u = smallest_unvisited()
    urow,ucol,dir,steps = u
    if (urow,ucol) == goal: break
    visited.add(u)   
   
    for v in neighbors(urow,ucol,dir,steps):
        if v not in visited:
            vrow,vcol,vdir,vsteps = v
            cost = dist[u] + city[vrow][vcol]
            if v not in dist or cost < dist[v]:
                dist[v] = cost
                prev[v] = u
    #print(len(visited),city.size)
    
on_path = set()
curr = u
total = 0
while True:
    cr,cc,cd,cs = curr
    if cr == 0 and cc == 0:
        break
    on_path.add((cr,cc))
    total += city[cr][cc]
    curr = prev[curr]
print(total)

with open("out2.txt","w") as f:
    for r in range(len(city)):
        for c in range(len(city[0])):
            if (r,c) in on_path:
                f.write(" ")
            else:
                f.write(str(city[r][c]))
        f.write("\n")         



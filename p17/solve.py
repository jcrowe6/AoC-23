import numpy as np
import heapq
import itertools

city = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        city.append(list(map(int,line[:-1])))
city = np.array(city)
print(city)
goal = (city.shape[0]-1,city.shape[1]-1)
#dist = {(0,0,'S',1):0} # dist[(a,b,c)] is dist of shortest path from source to (a,b) while moving c steps in a straight line previously

prev = {}
visited = set()

dist = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(dist, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while dist:
        priority, count, task = heapq.heappop(dist)
        if task is not REMOVED:
            del entry_finder[task]
            return task,priority
    raise KeyError('pop from an empty priority queue')

add_task((0,0,'S',0),0)

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
        out = [(0,1,'R',1),(1,0,'D',1)]
    else:
        for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
            if (dir == 'U' and r>row) or (dir == 'R' and c<col) or (dir == 'D' and r<row) or (dir == 'L' and c>col): continue
            if r >= 0 and r < len(city) and c >= 0 and c < len(city[0]):
                if r>row: # downward
                    if dir == 'L' or dir == 'R': out.append((r,c,'D',1))
                    # must be already moving D. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'D',steps+1))
                if r<row: # upward
                    if dir == 'L' or dir == 'R': out.append((r,c,'U',1))
                    # must be already moving U. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'U',steps+1))
                if c>col: # rightward
                    if dir == 'U' or dir == 'D': out.append((r,c,'R',1))
                    # must be already moving R. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'R',steps+1))
                if c<col: # leftward
                    if dir == 'U' or dir == 'D': out.append((r,c,'L',1))
                    # must be already moving L. if <3 steps, take 3rd and final step along this line
                    elif steps < 3: out.append((r,c,'L',steps+1))
    return out

# dijiktra's
while True:
    #u = smallest_unvisited()
    u,ucost = pop_task()
    urow,ucol,dir,steps = u
    if (urow,ucol) == goal: break
    visited.add(u)   
   
    for v in neighbors(urow,ucol,dir,steps):
        if v not in visited:
            vrow,vcol,vdir,vsteps = v
            cost = ucost + city[vrow][vcol]
            
            if v not in entry_finder or cost < entry_finder[v][0]:
                #dist[v] = cost
                add_task(v,cost)
                prev[v] = u
    if len(visited)%10000 == 0:
        print(len(visited),city.size*3*4)
    
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

with open("out6.txt","w") as f:
    for r in range(len(city)):
        for c in range(len(city[0])):
            if (r,c) in on_path:
                f.write(" ")
            else:
                f.write(str(city[r][c]))
        f.write("\n")         



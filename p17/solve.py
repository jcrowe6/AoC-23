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
dist = {(0,0):0} # dist[(a,b)] is dist of shortest path from source to (a,b)
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

def neighbors(row,col):
    out = []
    for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
        if r >= 0 and r < len(city) and c >= 0 and c < len(city[0]):
            out.append((r,c))
    return out

while len(visited) < city.size:
    u = smallest_unvisited()
    if u == goal: break
    visited.add(u)
    
    urow,ucol = u
    for v in neighbors(urow,ucol):
        if v not in visited:
            vrow,vcol = v
            cost = dist[u] + city[vrow][vcol]
            if v not in dist or cost < dist[v]:
                dist[v] = cost
                prev[v] = u
    #print(len(visited),city.size)
    
on_path = set()
curr = goal
while curr != (0,0):
    on_path.add(curr)
    curr = prev[curr]

with open("out.txt","w") as f:
    for r in range(len(city)):
        for c in range(len(city[0])):
            if (r,c) in on_path:
                f.write(" ")
            else:
                f.write(str(city[r][c]))
        f.write("\n")         



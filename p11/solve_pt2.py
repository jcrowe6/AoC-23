import numpy as np

g = []
rows_empty = set()
cols_empty = set()
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        g.append(list(map(lambda x: 1 if x == '#' else 0,line[:-1])))
galaxy = np.array(g)
r_i = 0
while r_i < galaxy.shape[0]:
    if galaxy[r_i,:].sum() == 0:
        rows_empty.add(r_i)
    r_i += 1
c_i = 0
while c_i < galaxy.shape[1]:
    if galaxy[:,c_i].sum() == 0:
        cols_empty.add(c_i)
    c_i += 1

print(rows_empty, cols_empty)

coords = []
r_expanded = 0
for r_i in range(len(galaxy)):
    if r_i in rows_empty:
        r_expanded += 1000000
    else:
        r_expanded += 1
    c_expanded = 0
    for c_i in range(len(galaxy[0])):
        if c_i in cols_empty:
            c_expanded += 1000000
        else:
            c_expanded += 1
        if galaxy[r_i,c_i] == 1:
            coords.append((r_expanded,c_expanded))
print(coords)

total = 0
for i in range(len(coords)-1):
    for j in range(i+1, len(coords)):
        r1,c1 = coords[i]
        r2,c2 = coords[j]
        diff = float(np.abs(r2-r1)+np.abs(c2-c1))
        total += diff
        print(total)
print(total)
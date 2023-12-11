import numpy as np

g = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        g.append(list(map(lambda x: 1 if x == '#' else 0,line[:-1])))
galaxy = np.array(g)
r_i = 0
while r_i < galaxy.shape[0]:
    if galaxy[r_i,:].sum() == 0:
        galaxy = np.insert(galaxy, r_i, 0, axis = 0)  
        r_i += 1
    r_i += 1
c_i = 0
while c_i < galaxy.shape[1]:
    if galaxy[:,c_i].sum() == 0:
        galaxy = np.insert(galaxy, c_i, 0, axis = 1)  
        c_i += 1
    c_i += 1

coords = []
for r_i in range(len(galaxy)):
    for c_i in range(len(galaxy[0])):
        if galaxy[r_i,c_i] == 1:
            coords.append((r_i,c_i))
print(len(coords))
total = 0
for i in range(len(coords)-1):
    for j in range(i+1, len(coords)):
        r1,c1 = coords[i]
        r2,c2 = coords[j]
        diff = np.abs(r2-r1)+np.abs(c2-c1)
        total += diff
print(total)

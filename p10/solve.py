map = []
st_pos = (0,0)
with open("input.txt") as f:
    i = 0
    while True:
        line = f.readline()
        if line == '': break
        map.append(list(line[:-1]))
        for j in range(len(line)):
            if line[j] == 'S':
                st_pos = (i,j)          
        i+=1



# given prev,curr,and a direction in L U R D, returns True if curr has been entered from prev by that direction
def entered_from(prev,curr,dir):
    prev_i,prev_j = prev
    curr_i,curr_j = curr
    if dir == 'L':
        return curr_j > prev_j
    elif dir == 'U':
        return curr_i > prev_i
    elif dir == 'R':
        return curr_j < prev_j
    elif dir == 'D':
        return curr_i < prev_i
    else:
        return "Bad input"


# given current and previous position, returns next position
def next_pos(prev_pos, curr_pos):
    prev_i,prev_j = prev_pos
    curr_i,curr_j = curr_pos
    curr_pipe = map[curr_i][curr_j]
    if curr_pipe == '|':
        if entered_from(prev_pos, curr_pos, 'U'): return (curr_i+1, curr_j)
        else: return (curr_i-1,curr_j)
    elif curr_pipe == '-':
        if entered_from(prev_pos, curr_pos, 'L'): return (curr_i, curr_j+1)
        else: return (curr_i, curr_j-1)
    elif curr_pipe == 'L':
        if entered_from(prev_pos, curr_pos, 'U'): return (curr_i, curr_j+1)
        else: return (curr_i-1, curr_j)
    elif curr_pipe == 'J':
        if entered_from(prev_pos, curr_pos, 'L'): return (curr_i-1, curr_j)
        else: return (curr_i, curr_j-1)
    elif curr_pipe == '7':
        if entered_from(prev_pos, curr_pos, 'L'): return (curr_i+1, curr_j)
        else: return (curr_i, curr_j-1)
    elif curr_pipe == 'F':
        if entered_from(prev_pos, curr_pos, 'R'): return (curr_i+1, curr_j)
        else: return (curr_i, curr_j+1)

# pick a direction to start down the path
cur_pos = None
st_i, st_j = st_pos
if map[st_i][st_j-1] in "-FL":
    cur_pos = (st_i, st_j-1)
elif map[st_i][st_j+1] in "-J7":
    cur_pos = (st_i,st_j+1)
elif map[st_i-1][st_j] in "|JL":
    cur_pos = (st_i-1,st_j)
elif map[st_i+1][st_j] in "|F7":
    cur_pos = (st_i+1,st_j)
else:
    print("Bad start pos")
    quit()
prev_pos = st_pos

loop = set([st_pos])
steps = 1 # we took one step to start already
while True:
    next = next_pos(prev_pos, cur_pos)
    next_i,next_j = next
    steps += 1
    loop.add(cur_pos)
    if map[next_i][next_j] == 'S':
        break
    prev_pos = cur_pos
    cur_pos = next
    
print("Steps to loop:",steps)
print("Half:", steps/2)

area = 0
for i in range(len(map)):
    j = 0
    in_loop_now = False
    while j < len(map[0]):
        if (i,j) in loop:
            if map[i][j] == '|': in_loop_now = not in_loop_now
            else:
                first_pipe = map[i][j]
                # skip ahead to next turn
                j += 1
                while map[i][j] == '-':
                    j += 1
                last_pipe = map[i][j]
                if first_pipe == 'F' and last_pipe == 'J': in_loop_now = not in_loop_now
                elif first_pipe == 'L' and last_pipe == '7': in_loop_now = not in_loop_now
        else:
            if in_loop_now:
                map[i][j] = 'X'
                area += 1
            else:
                map[i][j] = ' '
        j += 1

with open("out.txt", "w") as f:
    for line in map:
        f.write(''.join(line)+'\n')
print("area in loop:", area)


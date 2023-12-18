# this is essentially a palindrome finder
# idea: convert rows and columns into numbers, then search across them for the palindrome/reflection
# or just a single reflection point?
import numpy as np
# takes array of characters (either row or col) and converts them into a number by seeing it as a binary number
def arr_to_num(arr):
    p = 0
    total = 0
    for c in arr:
        if c == '#':
            total += 2**p
        p += 1
    return int(total)

# returns rows,cols numbers summarized as above
def map_to_nums(arr):
    rows = []
    for i in range(len(arr)):
        rows.append(arr_to_num(arr[i,:]))
    cols = []
    for j in range(len(arr[0,:])):
        cols.append(arr_to_num(arr[:,j]))
    return rows,cols

maps = []

def process_map(f):
    map_ = []
    while True:
        line = f.readline()
        if len(line) == 1 or len(line) == 0:
            maps.append(np.array(map_))
            return len(line)
        map_.append(list(line[:-1]))


with open("input.txt") as f:
    while True:
        if process_map(f) == 0: break

def find_reflect_i(map_):
    for i in range(len(map_)-1): # check for row-reflection
        if np.array_equal(map_[i,:],map_[i+1,:]):
            print("reflect after row",i+1)
            return 100*(i+1)
    for j in range(len(map_[0])-1): # check for col-reflection
        if np.array_equal(map_[:,j],map_[:,j+1]):
            print("reflect after col",j+1)
            return j+1


total = 0
for map_ in maps:
    print(map_)
    total += find_reflect_i(map_)
    input()
print(total)

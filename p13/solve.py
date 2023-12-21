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

def match_right(nums,stack):
    return stack == nums[-len(stack):]

def match_left(nums,stack):
    return stack == nums[:len(stack)]

# checks if the line of reflection lies after the ith row/colum
def reflects_over(arr, i):
    a = i
    b = i+1
    while a >= 0 and b < len(arr):
        if arr[a] != arr[b]: return False
        a -= 1
        b += 1
    return True 

# initially did very simple case of finding a single matching adjacent pair
# then did more complex idea of using a stack and popping off the top when there were matches.. couldn't get it to work.
# at this point, iterative search seems fine
def find_reflect_i(map_):
    rows,cols = map_to_nums(map_)
    for i in range(len(rows)-1):
        if reflects_over(rows, i):
            print("reflect after row",i+1)
            return 100*(i+1)
    for j in range(len(cols)-1):
        if reflects_over(cols, j):
            print("reflect after col",j+1)
            return j+1
            
    return "error!"



total = 0
for map_ in maps:
    print(map_)
    total += find_reflect_i(map_)
    #input()
print(total)

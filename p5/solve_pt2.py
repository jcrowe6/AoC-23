seeds = []
conversions = [] # list of lists of 3-tuples, loading the input in an easier to access form
first = True
with open("input.txt") as f:
    line = f.readline()
    seeds = list(map(int, line[7:-1].split(' ')))
    start,amt = seeds[::2],seeds[1::2]
    curr_conversion = []
    while True:
        line = f.readline()
        if line != '' and line[0] == '\n': continue
        
        if line == '' or line[0] not in "0123456789": # last conversion type ended
            if first: first = False # skip this for the first one, false alarm
            else: 
                conversions.append(curr_conversion)
                curr_conversion = []
                if line == '': break
        else:
            curr_conversion.append(list(map(int, line[:-1].split(' '))))
        
# almost 2 billion seeds is too many to run through this linear search with
# idea: build a single seed - location map

'''for conv in conversions:
    # see if ranges are contiguous
    print("new conv")
    conv.sort(key=lambda x: x[1])
    if conv[0][1] !=0: print("not starting at 0")
    last_end = conv[0][1]+conv[0][2]
    for e in conv[1:]:
        if e[1] != last_end: 
            print("gap", last_end,e[1], "size", e[1]-last_end)
        last_end = e[1] + e[2]
    
    conv.sort(key=lambda x: x[0])
    if conv[0][0] !=0: print("not starting at 0")
    last_end = conv[0][0]+conv[0][2]
    for e in conv[1:]:
        if e[0] != last_end: 
            print("gap", last_end, e[0], "size", e[0]-last_end)
        last_end = e[0] + e[2]'''

# Exploring the data, found some useful facts
# Each category's (seed, soil... location) numbers cover the range [0,4294967296)
# Each mapping has a gap that doesn't explicitly map numbers but keeps them the same
# So each new mapping "rearranges chunks of numbers" about the same interval. 
# Which would be easy to implement if we weren't looking at 4 billion individual number mappings. We need to exploit the range aspect of this

class SeedMap():
    def __init__(self, first_map):
        self.seed_map = first_map
    
    def update_with_next_map(self, next_map):
        self.seed_map.sort(key=lambda x: x[0]) # 
        next_map.sort(key = lambda x: x[1])
        print(self.seed_map)
        print(next_map)
        new_map = []
        # repeatedly pop both and construct brand new map?
        while True: # goal here is to go through all of prev seedmap's range and remake it 
            prev_map_front = self.seed_map.pop(0)
            next_map_front = next_map.pop(0)
            
            B_start_prev, A_start, prev_amt = prev_map_front
            C_start, B_start_next, next_amt = next_map_front

            print(f"A {A_start}-{A_start+prev_amt} maps to B {B_start_prev}-{B_start_prev+prev_amt} ({prev_amt})")
            print(f"B {B_start_next}-{B_start_next+next_amt} maps to C {C_start}-{C_start+next_amt} ({next_amt})")
            input()
            assert B_start_prev == B_start_next 
            assert B_start_prev < B_start_next+next_amt
            # 2 cases 
            # the prev category group is entirely mapped by the next category grouping
            if prev_amt < next_amt:
                new_map.append([C_start, A_start, prev_amt])
                next_map.insert(0, [C_start+prev_amt, B_start_next+prev_amt, next_amt-prev_amt])
            # the prev category group is partially mapped by this next category grouping and a future one
            elif prev_amt > next_amt:
                new_map.append([C_start, A_start, next_amt])
                self.seed_map.insert(0,[B_start_prev+next_amt,A_start+next_amt,prev_amt-next_amt])
                next_map.insert(0,[C_start+next_amt,B_start_next+next_amt,prev_amt-next_amt])
            else:
                new_map.append([C_start, A_start, next_amt])
                print("moving on")

            C_st, A_st, amt = new_map[-1]
            print(f"A {A_st}-{A_st+amt} maps to C {C_st}-{C_st+amt} ({amt})")
            input()




seedmap = SeedMap(conversions[0])
seedmap.update_with_next_map(conversions[1])

seeds = []
conversions = [] # list of lists of 3-tuples, loading the input in an easier to access form
first = True
with open("input.txt") as f:
    line = f.readline()
    seeds = list(map(int, line[7:-1].split(' ')))
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
            curr_conversion.append(tuple(map(int, line[:-1].split(' '))))

def convert(curr_value, convert_list):
    for next_st, prev_st, amt in convert_list:
        if curr_value >= prev_st and curr_value < prev_st+amt:
            return next_st + (curr_value - prev_st)
    return curr_value

def get_location(seed):
    curr = seed
    for conv_list in conversions:
        curr = convert(curr, conv_list)
    return curr

                

best_location = None
for seed in seeds:
    loc = get_location(seed)
    print(loc)
    if best_location is None or loc < best_location:
        best_location = loc

print("Closest possible location:",best_location)

# consider 3 lines at once...
# hardest part: avoid double counting.
# idea: scan for symbols -> lookahead for part numbers -> add and then mark number position to avoid double counting

# List(List) matrix of the input
engine = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        engine.append(list(line[:-1]))
shape = (len(engine), len(engine[0]))

# set of tuples (i,j) where engine[i][j] is the first digit of a part number to be added
marked_nums = set() 

digits = set("0123456789")

# given a location containing a digit, finds the location of the first digit then either
# returns -1 because this number has been processed before
# or
# processes the whole number by marking it in marked_nums and converts the entire number to an int and returns it.
def processNumber(i,j):
    while j != 0 and engine[i][j-1] in digits: # move j back as long as 1. we can 2. there is more number behind 
        j = j-1
    if (i,j) in marked_nums:
        return -1 # we've done this before!
    marked_nums.add((i,j))
    strnum = "" # concat digits into string and convert with int()
    while j != shape[1] and engine[i][j] in digits: # while j is valid and on a digit
        strnum += engine[i][j]
        j += 1
    return int(strnum)

# given a location of a possible gear in the engine, looks at all adjactent squares and processes the numbers
# that haven't been processed before, returning them all in a list
def processSymbol(i,j):
    results = []
    for i2 in [i-1, i, i+1]:
        for j2 in [j-1, j, j+1]:
            if ((i2 != i or j2 != j) and # skip the symbol
                    i2 >= 0 and i2 < shape[0] and j2 >= 0 and j2 < shape[1] and # check the bounds
                    engine[i2][j2] in digits): # check if there's a number there
                num = processNumber(i2,j2)
                if num != -1:
                    results.append(num)
    return results


            
total = 0
for i in range(len(engine)):
    for j in range(len(engine[0])):
        if engine[i][j] == '*': # maybe gear! 
            nums = processSymbol(i,j)
            if len(nums) == 2:
                ratio = nums[0]*nums[1]
                print(i,j,"has",nums,":",ratio)
                total += ratio

print("Sum of gear ratios:",total)

            



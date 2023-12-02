import re

# regex = re.compile(r'[0-9]')
# zero-width lookahead trick to get overlapping matches
pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))'
strtoint = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
total = 0

with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break

        matches = re.finditer(pattern, line) 
        nums = [match.group(1) for match in matches]
        
        first, last = nums[0], nums[-1]
        if first in strtoint: first = strtoint[first]
        if last in strtoint: last = strtoint[last]
        first, last = int(first), int(last)

        val = 10*first + last
        print(line[:-1], val)
        total += val

print("Total:", total)
        
import numpy as np
p1_total = 0

multipliers = np.ones(209)
i = 0
p2_total = 0

with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        # slices line, splits into list by spaces, filters out empty strings (caused by double spaces), and creates a set of just winning number strings
        winners = set(filter(None, line[10:39].split(' ')))
        # slices/splits/filters card numbers as before, then maps to 1 / 0 depending on if the number is in winning set, and sums.
        num_wins = sum(map(lambda x: 1 if x in winners else 0, filter(None, line[42:-1].split(' '))))
        
        p1_total += int(2**(num_wins-1)) # calculates score

        # part 2, straightforward solution for this small input
        multipliers[i+1 : i+1+num_wins] += 1*multipliers[i] 
        i += 1

print("Part 1 sum:", p1_total)
print("Part 2 sum:", int(multipliers.sum()))
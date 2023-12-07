from functools import cmp_to_key
from collections import Counter

hands = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        hand,bid = line[:-1].split(' ')
        hands.append((hand,int(bid)))

def get_type(hand):
    # improve to be best if J's are present
    counts = Counter(hand)
    j_amt = 0
    if 'J' in counts:
        if counts['J'] == 5: return 7
        j_amt = counts.pop('J')

        
    counts_sorted = sorted(list(counts.values()), reverse=True)
    counts_sorted[0] += j_amt
    
    biggest_group = counts_sorted[0]
    if biggest_group == 5:
        return 7
    elif biggest_group == 4:
        return 6
    elif biggest_group == 3:
        if counts_sorted[1] == 2:
            return 5
        else:
            return 4
    elif biggest_group == 2:
        if counts_sorted[1] == 2:
            return 3
        else:
            return 2
    else:
        return 1
    
let_to_val = {'T':10,'J':0,'Q':12,'K':13,'A':14}

def hand_cmp(a,b):
    a = a[0]
    b = b[0]
    a_type = get_type(a)
    b_type = get_type(b)
    if a_type < b_type:
        return -1
    elif a_type > b_type:
        return 1
    else:
        for acard, bcard in zip(a,b):
            aval = int(acard) if acard not in let_to_val else let_to_val[acard]
            bval = int(bcard) if bcard not in let_to_val else let_to_val[bcard]
            if aval < bval:
                return -1
            elif aval > bval:
                return 1
        return 0

hands.sort(key=cmp_to_key(hand_cmp))
total = 0
rank = 1
for h in hands:
    print(h)
    total += h[1]*rank
    rank+=1

print(total)

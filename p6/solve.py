times = [56, 97, 78, 75]
distances = [546, 1927, 1131, 1139]

def get_num_wins(time, record):
    wins = 0
    for presstime in range(time+1):
        dist = presstime*(time-presstime)
        if dist > record:
            wins += 1
    return wins

wins = [get_num_wins(time,rec) for time,rec in zip(times,distances)]
print(wins)
prod = 1
for win in wins:
    prod *= win
print("Product of wins:", prod)
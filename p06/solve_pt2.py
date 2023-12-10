time = 56977875
distance = 546192711311139

def get_num_wins(time, record):
    wins = 0
    for presstime in range(time+1):
        
        dist = presstime*(time-presstime)
        if dist > record:
            wins += 1
    return wins


print("Num wins:", get_num_wins(time, distance))
def extrapolate(hist):
    exps = [hist]
    i = 1
    while True:
        exp = []
        prev = exps[i-1]
        for a,b in zip(prev, prev[1:]):
            exp.append(b-a)
        i += 1
        exps.append(exp)
        if sum(exp) == 0:
            break
    ext = 0
    for i in range(len(exps)-1, 0, -1):
        ext = exps[i-1][-1] + exps[i][-1]
        exps[i-1].append(ext)
    return exps[0][-1]

print(extrapolate([0,   3,   6,   9,  12,  15]))

total = 0
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        inp = list(map(int,line[:-1].split(' ')))
        total += extrapolate(inp)
print(total)

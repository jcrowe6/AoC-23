colortomax = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# takes in a line of the input (without newline), processes it, and returns the game number as an int
# if it is a possible game, and 0 otherwise
def validGame(line):
    game, rest = line.split(":")
    gamenum = int(game.split(" ")[1])
    gamesets = rest.split("; ")

    for gs in gamesets:
        numcolors = gs.split(",")
        for numcolor in numcolors:
            if numcolor[0] == ' ': numcolor = numcolor[1:]
            num, color = numcolor.split(' ')
            num = int(num)
            if num > colortomax[color]:
                return 0
    return gamenum

total = 0
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        line = line[:-1]
        print(line)
        num = validGame(line)
        if num == 0: print("impossible game!")
        total += num

print("Sum of possible game numbers:", total)
        

        


        
        
# takes in a line of the input (without newline), processes it, and returns the power of the game
# (the product of the minimum number of cubes for each color for it to be a possible game)
def gamePower(line):
    game, rest = line.split(":")
    gamesets = rest.split("; ")

    colortomax = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for gs in gamesets:
        numcolors = gs.split(",")
        for numcolor in numcolors:
            if numcolor[0] == ' ': numcolor = numcolor[1:]
            num, color = numcolor.split(' ')
            num = int(num)
            if num > colortomax[color]:
                colortomax[color] = num
    print(colortomax)
    return colortomax["red"]*colortomax["blue"]*colortomax["green"]

total = 0
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == '': break
        line = line[:-1]
        print(line)
        power = gamePower(line)
        total += power

print("Sum of game powers:", total)
        

        


        
        
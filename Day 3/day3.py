with open("input.txt", "r") as f:
    rows = [line.split("\n")[0] for line in f.readlines()]

tmp = []
flag = False

total = 0

for j, row in enumerate(rows):
    for i, val in enumerate(row):
        if val.isdigit():
            tmp.append(val)
            for x in range (-1,2):
                for y in range (-1,2):
                    if x+i < 0 or x+i >= len(row): continue
                    if y+j < 0 or y+j >= len(rows): continue
                    if not rows[y+j][x+i].isdigit() and not rows[y+j][x+i] == ".":
                        flag = True
        else:
            if "".join(tmp) != "" and flag: total += int("".join(tmp))
            flag = False
            tmp =[]

print("Part 1:", total)

tmp = []
locs = []

total = 0

numbers = []
gears = []


for j, row in enumerate(rows):
    for i, val in enumerate(row):
        if val.isdigit():
            tmp.append(val)
            locs.append((y+j, x+i))
        else:
            if val == "*":
                gears.append((y+j, x+i))
            if "".join(tmp) != "": 
                [numbers.append(("".join(tmp), loc)) for loc in locs]
                locs = []
            flag = False
            tmp =[]

for j,i in gears:
    neighbors = []
    for x in range (-1,2):
        for y in range (-1,2):
            for num in numbers:
                if (y+j, x+i) == num[1] and num[0] not in neighbors:
                    neighbors.append(num[0])

    if len(neighbors) == 2:
        total += int(neighbors[0])*int(neighbors[1])
                    


print("Part 2:", total)
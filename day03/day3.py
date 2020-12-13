def path(map, changeX, changeY):
    x = 0
    y = 0
    count = 0
    while len(map) > y:
        if x >= len(map[0]):
            x -= len(map[0])

        if map[y][x] == "#":
            count += 1

        x += changeX
        y += changeY
    return count


map = []
with open('input.txt') as file:
    for line in file:
        line = list(line.strip('\n'))
        map.append(line)


print(path(map, 3, 1)+ path(map, 1, 1)*path(map, 3, 1) * path(map, 5, 1)* path(map, 7, 1)* path(map, 1, 2))
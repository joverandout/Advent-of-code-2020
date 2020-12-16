import math

memory = {}
mask = ''


file = open('input.txt', 'r').read()
splits = file.splitlines()
input_vals = [x.split(' = ') for x in splits]

def part2():
    for line in input_vals:
        if line[0] == 'mask':
            mask = line[1]
        else:
            key = int(line[0][4:-1])
            data = int(line[1])
            floating = []
            target = ''
            for x in range(36):
                next = mask[35-x]
                if next == '0':
                    next = str(key % 2)
                if next == 'X':
                    floating.append(35-x)
                target = next + target
                key = key//2
            for i in range(0, int(math.pow(2, len(floating)))):
                for index in floating:
                    target = target[:index] + str(i % 2) + target[index+1:]
                    i = i//2
                memory[int(target)] = data
    return sumvals(memory, 2)

def part1():
    for line in input_vals:
        if line[0] == 'mask':
            mask = line[1]
        else:
            key = int(line[0][4:-1])
            data = int(line[1])
            output = ""
            for x in range(36):
                next = mask[35-x]
                if next == 'X':
                    next = str(data % 2)
                output = next + output
                data = data//2
            memory[key] = output
    return sumvals(memory, 1)

def sumvals(memory, part):
    sum = 0
    for key in memory:
        if(part == 2):
            sum = sum+memory[key]
        else:
            sum = sum + int(memory[key], 2)
    return sum

print("++++++++++++++++++++++++")
print("|Part 1: " + str(part1())+"|")
memory = {}
mask = ''
print("|Part 2: " + str(part2())+" |")
print("++++++++++++++++++++++++")

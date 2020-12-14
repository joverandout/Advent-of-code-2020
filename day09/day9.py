import itertools

file = open('input.txt', 'r').read()
file = file.splitlines()
numbers = list(map(int, file))

def partA():
    for val in range(25, len(numbers)):
        boolean = False
        for smol_val in range(0, val):
            if numbers[val] - numbers[smol_val] in numbers[val-25:val]:
                boolean = True
        if not boolean:
            return(numbers[val], val)

def partB():
    import itertools
    numbers = []
    with open("input.txt") as f:
        for i in f.read().splitlines():
            numbers.append(int(i))

    goal = -1
    for i in range(25,len(numbers)):
        current = numbers[i]
        for a, b in itertools.combinations(numbers[i-25:i], 2):
            if a + b == current:
                break
        else:
            goal = current
    head = 0
    tail = 0
    while head <= len(numbers):
        current_list = numbers[tail:head]
        if len(current_list) < 2:
            head += 1
        sum_list = sum(current_list)
        if sum_list == goal:
            return(max(current_list) + min(current_list))
        elif sum_list < goal:
            head += 1
        elif sum_list > goal:
            tail += 1

print(partA())
print(partB())


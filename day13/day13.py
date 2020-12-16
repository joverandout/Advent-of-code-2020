data = [line.strip() for line in open("input.txt", 'r')]

departure_time = data[0]
values = data[1].split(',')
usedVals = []
finalValues = []

for val in values:
    if(val != "x"):
        usedVals.append(val)

for val in usedVals:
    time = 0
    while(time < int(departure_time)):
        time += int(val)
    finalValues.append(time)

bus = finalValues.index(min(finalValues))

print((finalValues[bus] - int(departure_time)) * int(usedVals[bus]))
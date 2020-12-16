data = [line.strip() for line in open("input.txt", 'r')]

def gcd(a,b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = gcd(b % a, a)
    return (g, x - (b // a) * y ,y)

def modu(n, p):
    g, inv, y = gcd(n, p)
    assert g == 1
    return inv % p

def chinese_remainder_theorem(buses, modulo):
    x = 0
    for a, p in buses:
        n = modulo // p
        inverse = modu(n, p)
        x = (x+a*n*inverse) % modulo
    return x % modulo

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

print("Part A: "+ str((finalValues[bus] - int(departure_time)) * int(usedVals[bus])))

def part2(buses):
    modulo = 1
    for i in buses:
        modulo *= i[1]
    return(chinese_remainder_theorem(buses, modulo))

part_2 = []
for counter, i in enumerate(data[1].split(',')):
    if i != "x":
        part_2.append((-counter, int(i)))
        
print("Part B: " + str(part2(part_2)))
import re
import datetime
import string

alphabet_lower = string.ascii_lowercase

rules = {}
count = 0
pos = [0, 0]
ids = []
first = ""

data = [line.strip() for line in open("input7.txt", 'r')]


def solve2(data):
    rules = {}
    for d in data:
        x = d[:-1].split(' contain ')
        currentColor = x[0][:-5]
        for b in x[1].split(', '):
            if b != 'no other bags':
                color = ' '.join(b.split(' ')[1:-1])
                num = int(b.split(' ')[0])
                if currentColor not in rules:
                    rules[currentColor] = set({})
                rules[currentColor].add((color, num))
            else:
                rules[currentColor] = set({})

    def add_colors(color):
        total = 0
        
        for o_color, num in rules[color]:
            total += num * (1 + add_colors(o_color))
        return total

    print(add_colors('shiny gold'))

    
def a():
    import re
    checked = set()

    def parse_rules(puzzle_input):
        rules = {}
        for line in puzzle_input.splitlines():
            color, contents_text = line.split(' bag contain ')
            items = re.findall(r'(\d+) ([^,]+) bag', contents_text)
            rules[color] = [(int(n), inner) for n, inner in items]
        return rules

    def contains(color, rules, target):
        if color in checked:
            return True
        contents = rules[color]
        does_contain = any(
            inner_colour == target or contains(inner_colour, rules, target) for _, inner_colour in contents
        )
        if does_contain:
            checked.add(color)
        return does_contain

    def count_containers_of(target, rules):
        count = 0
        for color in rules:
            if contains(color, rules, target):
                count += 1
        return count

    file = open('input7.txt', 'r').read().replace("bags", "bag")
    rules = parse_rules(file)
    return(count_containers_of("shiny gold", rules))

def solve(color):
    ans = 1
    for count, subcol in f[color]:
        ans += count * solve(subcol)

print(a())
print(b(rules, "shiny gold", 1), -1)
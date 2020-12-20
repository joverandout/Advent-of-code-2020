def check(ruleSet, sequence, input):
    if not sequence:
        yield input
    else:
        index, *sequence = sequence
        for input in run(ruleSet, index, input):
            yield from check(ruleSet, sequence, input)

def fetch_rules(line, rawRules):
    k, rule = line.split(': ')
    if rule[0] == '"':
        rule = rule[1:-1]
    else:
        rule = [sequence.split(' ') if ' ' in sequence else [sequence]
                for sequence in (rule.split(' | ') if ' | ' in rule else [rule])]
    return rule, k

def expand(ruleSet, alt, string):
    for sequence in alt:
        yield from check(ruleSet, sequence, string)


def run(ruleSet, index, string):
    if isinstance(ruleSet[index], list):
        yield from (expand(ruleSet, ruleSet[index], string))
    else:
        if string and string[0] == ruleSet[index]:
            yield string[1:]

def part1(rules, strings):
    return sum(any(m == '' for m in run(rules, '0', s)) for s in strings)

def part2(rules, strings):
    rules = {**rules, '8': [['42'], ['42', '8']],
             '11': [['42', '31'], ['42', '11', '31']]}
    return sum(any(m == '' for m in run(rules, '0', s)) for s in strings)

with open("input.txt", 'r') as file:
        rawRules, rawStrings = file.read().split("\n\n")
        rules = {}
        for line in rawRules.split('\n'):
            rule, k = fetch_rules(line, rawRules)
            rules[k] = rule
        strings = rawStrings.split("\n")#
print("++++++++++")
print("Part 1:" + str(part1(rules, strings)))
print("Part 2:" + str(part2(rules, strings)))
print("++++++++++")


import copy

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def run(instructions: list) -> [bool, int]:
    accumulator = 0
    visited = [False for _ in instructions]
    ix = 0
    while (0 <= ix < len(instructions)) and (not visited[ix]):
        visited[ix] = True
        operation, arg = instructions[ix]
        if operation == ACC:
            accumulator += arg
            ix += 1
        elif operation == JMP:
            ix += arg
        elif operation == NOP:
            ix += 1
    is_terminated = ix == len(instructions)
    return is_terminated, accumulator

with open('input08.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    instructions = []
    for line in inputs:
        operation, arg = line.split(' ')
        instructions.append([operation, int(arg)])
    _, part_a = run(instructions)
    print(part_a)
    for ix, instruction in enumerate(instructions):
        operation, arg = instruction
        if operation in (NOP, JMP):
            instructions_copy = copy.deepcopy(instructions)
            instructions_copy[ix][0] = JMP if operation == NOP else NOP

            is_terminated, accumulator = run(instructions_copy)
            if is_terminated:
                print(accumulator)

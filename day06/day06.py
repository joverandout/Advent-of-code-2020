from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys

def get_input():
    with open("6.txt", 'r') as input_file:
        numbers = input_file.readlines()
    return numbers

def b():
    part2 = 0
    fin = open("6.txt", "r")
    blocks = fin.read().split("\n\n")
    for block in blocks:
        x = len(block.split())
        c = Counter(block)
        part2 += sum(v == x for _, v in c.items())
        if c['\n'] == x:
            part2 -= 1
    return part2

def a():
    input = get_input()
    count = 0
    letters = []

    for line in input:
        if line == '\n':
            count += len(letters)
            letters = []
        else:
            line = line.rstrip()
            for character in line:
                if character not in letters:
                    letters.append(character)

    return count + len(letters)

print(a())
print(b())
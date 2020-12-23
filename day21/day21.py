from __future__ import annotations
from collections import defaultdict
import math
import datetime
from typing import NamedTuple, Set, List, Dict

def main():
    with open('input.txt') as file:
        raw = file.read()
        input = [Food_item.parse(line) for line in raw.split("\n")]
        print("part 1: " + str(part1(input)))
        cands = candidates(input)
        print("part 2: " + str(reorder(cands)))

class Food_item(NamedTuple):
    ingredients: List[str]
    allergens: List[str]

    @staticmethod
    def parse(line: str) -> Food_item:
        parts = line.split("(contains ")
        if len(parts) == 1:
            allergens = []
        else:
            allergens = parts[1][:-1].split(", ")
        return Food_item(parts[0].split(), allergens)

def candidates(input: List[Food_item]) -> Dict[str, Set[str]]:
    candidates: Dict[str, Set[str]] = {}

    for Food_item in input:
        for allergen in Food_item.allergens:
            if allergen not in candidates:
                candidates[allergen] = set(Food_item.ingredients)
            else:
                candidates[allergen] = candidates[allergen] & set(Food_item.ingredients)

    allergens = list(candidates)
    keep_going = True

    while keep_going:
        keep_going = False
        known = {allergen: cands for allergen, cands in candidates.items()
                 if len(cands) == 1}
        taken_ingredients = {ingredient for cands in known.values() for ingredient in cands}
        for allergen in allergens:
            if allergen not in known and (candidates[allergen] & taken_ingredients):
                keep_going = True
                candidates[allergen] = candidates[allergen] - taken_ingredients

    return candidates 


def reorder(candidates: Dict[str, Set[str]]) -> str:
    assert all(len(s) == 1 for s in candidates.values())

    return ",".join(next(iter(cands)) for allergen, cands in sorted(candidates.items()))

def part1(input: List[Food_item]) -> int:
    cands = candidates(input)
    can_contain = {ingredient for cands in cands.values() for ingredient in cands}

    return sum(ingredient not in can_contain
                for Food_item in input
                for ingredient in Food_item.ingredients)


main()

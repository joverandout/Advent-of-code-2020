
from typing import Dict, List
import re

passports = Dict[str, str]

def make_passport(raw: str) -> passports:
    lines = raw.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    passport = {}

    for line in lines:
        for chunk in line.split(" "):
            key, value = chunk.split(":")
            passport[key] = value

    return passport

def make_passports(raw: str) -> List[passports]:
    chunks = raw.split("\n\n")
    return [make_passport(chunk) for chunk in chunks if chunk.strip()]

DEFAULT_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate(passport: passports, 
             required_fields: List[str] = DEFAULT_FIELDS) -> bool:
    return all(field in passport for field in required_fields)

def height(hgt: str) -> bool:
    if hgt.endswith('cm'):
        hgt = hgt.replace('cm', '')
        try:
            return 150 <= int(hgt) <= 193
        except:
            return False
    elif hgt.endswith("in"):
        hgt = hgt.replace("in", "")
        try:
            return 59 <= int(hgt) <= 76 
        except:
            return False

    return False

def validate2(passport: passports) -> bool:
    rules = [
        1920 <= int(passport.get('byr', -1)) <= 2002,
        2010 <= int(passport.get('iyr', -1)) <= 2020,
        2020 <= int(passport.get('eyr', -1)) <= 2030,
        height(passport.get('hgt', '')),
        re.match(r"^#[0-9a-f]{6}$", passport.get('hcl', '')),
        passport.get('ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        re.match(r"^[0-9]{9}$", passport.get('pid', ''))
    ]

    return all(rules)



with open('day4input.txt') as f:
    passports = make_passports(f.read())
    print(sum(validate(passport) for passport in passports))
    print(sum(validate2(passport) for passport in passports))
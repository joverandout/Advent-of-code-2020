import re
import string

def concat(first, last, sum):
    total = ""
    for i in range(first, last+1):
        total = total + sum[i]
    return total
    
def countbracs(line):
    for char in line:
        if char == "(" or char == ")":
            return True
    return False

def do_sum(sum):
    expr = []
    first = 0
    for i in range(0, len(sum)):
        if sum[i] == " ":
            expr.append(str(concat(first, i-1, sum)))
            first = i+1
    expr.append(str(concat(first, len(sum)-1, sum)))
    value = int(expr[0])
    for i in range(1, len(expr), 2):
        op = expr[i]
        if op == "+":
            value = value + int(expr[i+1])
        elif op == "*":
            value = value * int(expr[i+1])
        else:
            raise ValueError(f"bad op: {op}")
    return value

def get_number_of_brackets(line):
    bracs = []
    for char in line:
        if char == "(" or char == ")":
            bracs.append(char)
    return bracs

def eval_line(line, bracket_order):
    for i in range(len(bracket_order)):
        if bracket_order[i] == "(" and bracket_order[i+1] == ")":
            return(eval_bracket(line, i))

def eval_bracket(line, bracket_index):
    index1 = 0
    index2 = 0
    firstBrac = False
    bracket_index2 = -1
    for count in range(len(line)):
        if line[count] == "(":
            bracket_index2 += 1
            if(bracket_index2 == bracket_index):
                index1 = count
                firstBrac = True
        if(firstBrac == True and line[count] == ")"):
            index2 = count-1
            break
    if(version2 == False):
        swap_val = do_sum(line[index1+1:index2+1])
    else:
        swap_val = do_sum2(line[index1+1:index2+1])
    new_line = ""
    done = False
    for i in range(len(line)):
        if i<index1 or i > index2+1:
            new_line += line[i]
        elif(done == False):
            done = True
            new_line += str(swap_val)
    return new_line

def do_sum2(sum):
    expr = []
    first = 0
    for i in range(0, len(sum)):
        if sum[i] == " ":
            expr.append(str(concat(first, i-1, sum)))
            first = i+1
    expr.append(str(concat(first, len(sum)-1, sum)))
    while len(expr) > 1:
        if "+" in expr:
            i = expr.index("+")
            new_val = int(expr[i-1]) + int(expr[i+1])
            expr = expr[:i-1] + [str(new_val)] + expr[i+2:]
        else:
            stringy = ""
            for a in range(len(expr)):
                stringy += expr[a]
                if(a != len(expr)-1):
                    stringy += " "
            return do_sum(stringy)

    return int(expr[0])

total = 0
version2 = False
with open("input.txt") as f:
    lines = f.read().splitlines()
for line in lines:
    line2 = line
    while(countbracs(line2) == True):
        line2 = eval_line(line2, get_number_of_brackets(line2))
    line2 = do_sum(line2)
    total = total + line2
print(total)
version2 = True
total = 0
with open("input.txt") as f:
    lines = f.read().splitlines()
for line in lines:
    line2 = line
    while(countbracs(line2) == True):
        line2 = eval_line(line2, get_number_of_brackets(line2))
    line2 = do_sum2(line2)
    total = total + line2
print(total)
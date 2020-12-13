numberValid = 0
numberValid2 = 0

with open('input.txt') as file:
    for line in file:
        elements = line.strip("\n").split(" ")

        rules = elements[0].split("-")
        minimum = int(rules[0])
        maximum = int(rules[1])

        letter = elements[1].strip(":")
        password = elements[2]

        miniCount = 0

        print(letter + "-" + str(minimum) + "-" + str(maximum))

        for char in range(0, len(password)):
            if(password[char] == letter):
                miniCount+=1
                if(miniCount > maximum):
                    numberValid += 1
                    break

        if(miniCount < minimum):
            numberValid += 1

        if(password[minimum-1] != letter and password[maximum-1] != letter):
            numberValid2 += 1
        elif(password[minimum-1] == letter and password[maximum-1] == letter):
            numberValid2 +=1


    print(1000 - numberValid)
    print(1000 - numberValid2)
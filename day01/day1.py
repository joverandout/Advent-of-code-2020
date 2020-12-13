import csv

def main():
    data = []
    with open("day1input.txt", "r") as file:
        for line in file:
            data.append(int(line))

    print(partA(data))
    print(partB(data))

def partA(data):
    data.sort()
    for i in range(len(data)):
        j = len(data)-1
        while (data[i]+data[j]) >= 2020:
            if (data[i]+data[j]) == 2020:
                return data[i]*data[j]
            elif data[i]+data[j] > 2020:
                j -= 1
    return 0

def partB(data):
    second_data = set()
    third_data = set()
    for i in data:
        for j in second_data:
            for k in third_data:
                if i+j+k == 2020:
                    return i*j*k
            third_data.add(i)
        second_data.add(i)

if __name__ == "__main__":
    main()
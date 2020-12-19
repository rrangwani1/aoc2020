with open("day2input.txt") as f:
    content = f.readlines()
for i in range(len(content)):
    content[i] = content[i].split(" ")
    content[i][0] = content[i][0].split("-")
    content[i][1] = content[i][1].strip(":")
    content[i][2] = content[i][2].strip()
#print(content)


def part1():
    valid_count = 0

    for pwd in content:
        min = int(pwd[0][0])
        max = int(pwd[0][1])
        letter = pwd[1]
        passcode = pwd[2]

        if passcode.count(letter) >= min and passcode.count(letter) <= max:
            valid_count += 1

    return valid_count


def part2():
    valid_count = 0

    for pwd in content:
        index1 = int(pwd[0][0]) - 1
        index2 = int(pwd[0][1]) - 1
        letter = pwd[1]
        passcode = pwd[2]

        first_spot = True if passcode[index1]==letter else False
        second_spot = True if passcode[index2] == letter else False

        if (first_spot and not second_spot) or (not first_spot and second_spot):
            valid_count += 1

    return valid_count



if __name__ == "__main__":
    print(part1())
    print(part2())
with open("day4input.txt") as f:
    content_pre = []
    text = ""
    for line in f:
        if line == "\n":
            content_pre.append(text)
            text = ""
        else:
            text = text + " " + line.strip()
    content = []
    for line in content_pre:
        line1 = line.strip(" ").split(" ")
        temp_dict = dict()
        for item in line1:
            piece = item.split(":")
            temp_dict[piece[0]] = piece[1]

        content.append(temp_dict)


def part1():
    valid = 0
    for person in content:
        if (len(person.keys()) == 8) or (len(person.keys()) == 7 and 'cid' not in person.keys()):
            valid += 1

    return valid


def part2():

    valid = 0
    for person in content:
        byr_true = False
        iyr_true = False
        eyr_true = False
        hgt_true = False
        hcl_true = False
        ecl_true = False
        pid_true = False
        if (len(person.keys()) == 8) or (len(person.keys()) == 7 and 'cid' not in person.keys()):
            byr = int(person['byr'])
            if 1920 <= byr <= 2002:
                byr_true = True

            iyr = int(person['iyr'])
            if 2010 <= iyr <= 2020:
                iyr_true = True

            eyr = int(person['eyr'])
            if 2020 <= eyr <= 2030:
                eyr_true = True

            units = person['hgt'][-2:]
            vals = person['hgt'][:-2]
            if units == 'cm' or units == 'in':
                if ((units == 'in' and (59 <= int(vals) <= 76)) or (units == 'cm' and (150 <= int(vals) <= 193))):
                    hgt_true = True
            # if hgt_true == True:
            #     print(units + vals)

            hcl = person['hcl']
            tmp_bool = False
            if (len(hcl) == 7) and (hcl[0] == "#"):
                rest = hcl[1:7]
                tmp_bool = True
                for ch in rest:
                    if not ((97 <= ord(ch) <= 102) or (48 <= ord(ch) <= 57)):
                        tmp_bool = False
                        break
            hcl_true = tmp_bool

            ecl = person['ecl']
            if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                ecl_true = True

            pid = person['pid']
            tmp_bool = True
            for ch in pid:
                if not (48 <= ord(ch) <= 57):
                    tmp_bool = False
                    break
            if len(pid) != 9:
                tmp_bool = False
            pid_true = tmp_bool

        if byr_true and iyr_true and eyr_true and hgt_true and hcl_true and ecl_true and pid_true:
            valid += 1
        #     print("True: ")
        #     print(person)
        # else:
        #     print("false: ")
        #     print(person)
    return valid

if __name__ == "__main__":
    print(part1())
    print(part2())
# Day 1 AoC

with open("day1input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

def part1():

    sum = 2020
    minus_dict = dict()
    val1 = 0

    for val in content:
        minus_dict[val] = sum-val

    for val in minus_dict.values():
        if val in minus_dict.keys():
            val1 = val
            break

    val2 = 2020-val1
    mult = val1*val2
    print(str(val1) + " and " + str(val2) + " = " + str(val1+val2) + " where multiple is " + str(mult))


def part2():
    sum = 2020
    val1 = 0
    val2 = 0
    val3 = 0
    for i in range(0, len(content)-1):
        val_set = set()
        cur_sum = sum-content[i]
        for j in range(i+1, len(content)):
            if (cur_sum-content[j]) in val_set:
                val1 = content[i]
                val2 = content[j]
                val3 = sum-(val1+val2)
                out="values are: {}, {}, {}. Sum is {}, mult is {}".format(val1,val2,val3,(val1+val2+val3),(val1*val2*val3))
                print(out)
                return

            val_set.add(content[j])
    print('fail')
    return


if __name__ == "__main__":
    #part1()
    part2()
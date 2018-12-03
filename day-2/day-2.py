from itertools import combinations

with open("input") as input:
    lines = input.readlines()
    IDs = [line.strip() for line in lines]

# Part 1
two_letters = 0
three_letters = 0

for ID in IDs:
    chars = dict()
    for c in ID:
        if c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1

    is_two_letter = False
    is_three_letter = False
    for v in chars.values():
        if (v == 2) & (not is_two_letter):
            two_letters += 1
            is_two_letter = True
        elif (v == 3) & (not is_three_letter):
            three_letters += 1
            is_three_letter = True

        if is_three_letter and is_two_letter:
            break

checksum = two_letters * three_letters

print(f"Part 1: {two_letters} * {three_letters} = {checksum}")

# Part 2
ID_length = len(IDs[0])

for (ID_1, ID_2) in combinations(IDs, 2):
    comparison = [a == b for (a, b) in zip(list(ID_1), list(ID_2))]
    if sum(comparison) == (ID_length - 1):
        output = []
        for c, b in zip(list(ID_1), comparison):
            if b:
                output.append(c)
        print(f"Part 2: {''.join(output)}")
        break

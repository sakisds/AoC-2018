from itertools import cycle

# Part 1
frequency = 0
with open("input") as input:
    for line in input:
        frequency += int(line)

print(f"Part 1: {frequency}")

# Part 2
frequency = 0
frequencies = set([0])

with open("input") as input:
    for line in cycle(input):
        frequency += int(line)
        if frequency in frequencies:
            print(f"Part 2: {frequency}")
            break
        frequencies.add(frequency)

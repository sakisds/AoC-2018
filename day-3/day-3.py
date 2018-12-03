from typing import NamedTuple
import numpy as np
from matplotlib import pyplot


class Claim(NamedTuple):
    id: str
    x: int
    y: int
    width: int
    height: int


# Parse input
with open("input") as input_file:
    raw_input = input_file.readlines()

claims = []
for line in raw_input:
    tokens = line.strip().split(' ')

    id = tokens[0][1:]
    (x, y) = tokens[2][:-1].split(',')
    (width, height) = tokens[3].split('x')

    claims.append(
        Claim(
            id=int(id),
            x=int(x), y=int(y),
            width=int(width), height=int(height)
        )
    )

# Part 1
area = np.ndarray([1000, 1000], dtype=int)

for claim in claims:
    area[
        claim.x:(claim.x + claim.width),
        claim.y:(claim.y + claim.height)
    ] += 1

print(f"Part 1: {sum(sum(area >= 2))}")

# Part 2
for claim in claims:
    claim_area = area[
        claim.x:(claim.x + claim.width),
        claim.y:(claim.y + claim.height)
    ]

    # Check if it overlaps with anything else
    if claim_area.max() == 1:
        print(f"Part 2: ID #{claim.id}")
        break

# Plot
pyplot.pcolormesh(area)
pyplot.show()

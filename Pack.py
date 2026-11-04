# This is where i program the dynamic programming algorithm to find the best combination of items to put in the bag.

from Bag import *

rows = len(stuff) + 1
cols = 6

grid = []

for _ in range(rows):
    row = [0] * cols
    grid.append(row)

r = 1
for item in stuff:
    for c in range(1, cols):
        slots = stuff[item]["slots"]
        points = stuff[item]["points"]
        skip = grid[r-1][c]
        if stuff[item]["slots"] <= c:
            left = c - slots
            take = points + grid[r-1][left]
            grid[r][c] = max(skip, take)
        else:
            grid[r][c] = skip        
    r += 1

r = rows - 1
c = bag
taken = []

while r > 0:
    if grid[r][c] != grid[r-1][c]:
        name = list(stuff)[r-1]
        taken.append(name)
        c = c - stuff[name]["slots"]
    r = r - 1


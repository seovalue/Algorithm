import sys
import itertools

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

for dwarf in itertools.combinations(dwarfs,7):
    if sum(dwarf) == 100:
        dwarf = sorted(dwarf)
        for d in dwarf:
            print(d)
        exit()
with open("day 1\input.txt", "r") as f:
    calories = f.readlines()

total_cal = []
current = 0

for cal in calories:
    if cal == "\n":
        total_cal.append(current)
        current = 0
    else:
        current += int(cal)

print(max(total_cal))  # solution for part 1
print(sum(sorted(total_cal)[:-4:-1]))  # solution for part 2
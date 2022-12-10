# part 1
x = 1
cycle_number = 0
target_cycles = [20, 60, 100, 140, 180, 220]
cycle_result = []
instructions = {
    "addx": 2,
    "noop": 1
}
# part 2
crt_screen = [list("." * 40) for _ in range(6)]
crt_lines = [40, 80, 120, 160, 200, 240]
row = 0
current_index = 0

with open("day 10/input.txt") as f:
    for line in f.readlines():
        line = line.split()
        
        pixel_pos = (x - 1, x, x + 1)
        
        for i in range(instructions[line[0]]):
            cycle_number += 1
            
            if current_index in pixel_pos:
                crt_screen[row][current_index] = "#"
                
            if cycle_number == crt_lines[row]:
                current_index = 0
                row += 1
            else:
                current_index += 1
            
            if cycle_number in target_cycles:
                cycle_result.append(cycle_number * x)
        
            if line[0] == "addx" and i == 1:
                x += int(line[1])

print(sum(cycle_result))
for i in crt_screen:
    print(''.join(i))

from time import perf_counter

start = perf_counter()

with open("inputs/input14.txt") as f:
    cave_map = set()
    
    for line in f.readlines():
        pos_list = line.strip().split(" -> ")
        
        for i in range(len(pos_list) - 1):
            first_point = pos_list[i]
            second_point = pos_list[i + 1]
            
            x1, y1 = int(first_point.split(",")[0]), int(first_point.split(",")[1])
            x2, y2 = int(second_point.split(",")[0]), int(second_point.split(",")[1])
            
            cave_map.add((x1, y1))
            
            while x1 != x2 or y1 != y2:
                if x1 != x2:
                    if x1 < x2:
                        x1 += 1
                    elif x1 > x2:
                        x1 -= 1            
                elif y1 != y2:
                    if y1 < y2:
                        y1 += 1
                    elif y1 > y2:
                        y1 -= 1
                
                cave_map.add((x1, y1))
                
# defining the limits
limits = sorted(cave_map)
limits = limits[0][0], limits[-1][0]
floor = sorted(cave_map, key=lambda x: x[1])
floor = floor[-1][1] + 2

start_point = (500, 0)
inbound = True
sand_count = 0

while inbound:
    rest = False
    x, y = start_point

    if (x, y) in cave_map:
        break
    
    while not rest:
        # limits for part 1
        # if x < limits[0] or x > limits[1]:
        #             inbound = False
        #             rest = True
        
        if (x, y + 1) not in cave_map and y + 1 < floor:
            y += 1
        
        elif (x, y + 1) in cave_map  and y + 1 < floor:
            if (x - 1, y + 1) not in cave_map:
                x -= 1
                y += 1  
            elif (x + 1, y + 1) not in cave_map:
                x += 1
                y + 1
            else:
                cave_map.add((x, y))
                rest = True
                sand_count += 1
        else:
            cave_map.add((x, y))
            rest = True
            sand_count += 1

print(sand_count)
end = perf_counter()

print("time to run:", end - start)

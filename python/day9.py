head = (0, 0)
tail = (0, 0)

traversed_pos = set()
traversed_pos.add((0, 0))
traversed_pos_rope = set()
traversed_pos_rope.add((0, 0))

rope = [(0, 0) for _ in range(10)]

direction_dict = {"U": (1, 0),
                  "D": (-1, 0),
                  "R": (0, 1),
                  "L": (0, -1)}

with open("inputs/input9.txt") as f:
    for line in f.readlines():
        direction, distance = line.split()[0], int(line.split()[1])
        direction_x, direction_y = direction_dict[direction]
        
        for i in range(distance):
            head_x, head_y = head
            head_x, head_y = head_x + direction_x, head_y + direction_y
            
            if abs(head_x - tail[0]) >= 2 or abs(head_y - tail[1]) >= 2:
                tail = head
                traversed_pos.add(tail)
            
            head = (head_x, head_y)
                
print(len(traversed_pos))

with open("inputs/input9.txt") as f:
    for line in f.readlines():
        direction, distance = line.split()[0], int(line.split()[1])
        direction_x, direction_y = direction_dict[direction]
        
        for i in range(distance):
            head_x, head_y = rope[0]
            head_x, head_y = head_x + direction_x, head_y + direction_y
            rope[0] = (head_x, head_y)
            
            for j in range(9):
                hx, hy = rope[j]
                tail_x, tail_y = rope[j + 1]
                
                if abs(hx - tail_x) >= 2 or abs(hy - tail_y) >= 2:
                    diff_x, diff_y = 1, 1
                    
                    if hx - tail_x == 0:
                        diff_x = 0
                    elif hx - tail_x < 0:
                        diff_x = -1
                    if hy - tail_y == 0:
                        diff_y = 0
                    elif hy - tail_y < 0:
                        diff_y = -1
                                     
                    rope[j + 1] = (tail_x + diff_x, tail_y + diff_y)
                    
                    if j == 8:
                        traversed_pos_rope.add(rope[j + 1])
                       
print(len(traversed_pos_rope))        

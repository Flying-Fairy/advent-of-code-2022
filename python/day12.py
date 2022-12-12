with open("inputs/input12.txt") as f:
    heightmap = []
    
    for line in f.readlines():
        heightmap.append(list(line.strip()))

possible_start = []
start = []

for r_index, row in enumerate(heightmap):
    for c_index, col in enumerate(row):
        if c_index == 0:
            possible_start.append(((r_index, c_index), 0))
        if col == "S":
            start.append(((r_index, c_index), 0))


def get_neighbors(pos, heightmap):
    x, y = pos
    neighbors = []
    
    if x > 0:  # up
        neighbors.append((x - 1, y))
    if x < len(heightmap) - 1:  # down
        neighbors.append((x + 1,  y))
    if y > 0:  # left
        neighbors.append((x, y - 1))
    if y < len(heightmap[x]) - 1:  # right
        neighbors.append((x, y + 1))
    
    return neighbors

def find_shortest_path(start, heightmap):
    queue = start
    visited = set()

    while queue:
        pos, dist = queue.pop(0)
        x, y = pos
        current_char = heightmap[x][y]
        
        if current_char == "E":
            return dist
        
        for neighbor in get_neighbors(pos, heightmap):
            current_height = ord(current_char)
            if neighbor not in visited:
                nx, ny = neighbor
                
                if heightmap[nx][ny] == "E":
                    neighbor_height = ord("z")
                else:
                    neighbor_height = ord(heightmap[nx][ny])

                if current_height + 1 >= neighbor_height or current_char == "S":
                    queue.append((neighbor, dist + 1))
                    visited.add(neighbor)
        
        visited.add(pos)
            
print(find_shortest_path(start, heightmap))  # part 1
print(find_shortest_path(possible_start, heightmap))  # part 2
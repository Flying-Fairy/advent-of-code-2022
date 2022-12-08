with open("day 8/input.txt") as f:
    tree_patch = []
    for line in f.readlines():
        tree_patch.append(list(line.strip()))

visible_trees = 0

def check_visible(ls, tree_pos, tree_height, direction):
    x, y = tree_pos
    tree_score = {
        "up":0,
        "down": 0,
        "left": 0,
        "right": 0
        }
    
    if direction == "up":
        while x > 0:
            x -= 1
            current = ls[x][y]
            if tree_height > current:
                tree_score["up"] += 1
            else:
                tree_score["up"] += 1
                return False, tree_score["up"]
        
        return True, tree_score["up"]

    elif direction == "down":
        while x < len(ls) - 1:
            x += 1
            current = ls[x][y]
            if tree_height > current:
                tree_score["down"] += 1
            else:
                tree_score["down"] += 1
                return False, tree_score["down"]
        
        return True, tree_score["down"]
    
    elif direction == "left":
        while y > 0:
            y -= 1
            current = ls[x][y]
            if tree_height > current:
                tree_score["left"] += 1
            else:
                tree_score["left"] += 1
                return False, tree_score["left"]
        
        return True, tree_score["left"]

    elif direction == "right":
        while y < len(ls[x]) - 1:
            y += 1
            current = ls[x][y]
            if tree_height > current:
                tree_score["right"] += 1
            else:
                tree_score["right"] += 1
                return False, tree_score["right"]
        
        return True, tree_score["right"]
    
scenic_scores = []

for r_index, row in enumerate(tree_patch):
    for c_index, col in enumerate(row):
        pos = (r_index, c_index)
        height = tree_patch[pos[0]][pos[1]]
        if r_index == 0 or r_index == len(tree_patch) - 1 or c_index == 0 or c_index == len(row) - 1:
            visible_trees += 1
        else:
            up, up_score = check_visible(tree_patch, pos, height, "up")
            down, down_score = check_visible(tree_patch, pos, height, "down")
            left, left_score = check_visible(tree_patch, pos, height, "left")
            right, right_score = check_visible(tree_patch, pos, height, "right")
            
            if up or down or left or right:
                visible_trees += 1
            
            score = up_score * down_score * left_score * right_score
            scenic_scores.append(score)

print(visible_trees)
print(max(scenic_scores))

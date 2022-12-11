with open("inputs/input7.txt") as f:
    dir_stack = []
    dir_sizes = {}
    
    for line in f.readlines():
        line = line.split()
    
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] != "..":
                    if not dir_stack:
                        dir_sizes[line[2]] = {"size": 0}
                        dir_stack.append(dir_sizes[line[2]])
                    else:
                        dir_stack[-1][line[2]] = {"size": 0}
                        dir_stack.append(dir_stack[-1][line[2]])
                else:
                    dir_stack.pop() 
        
        elif line[0] != "dir":
            dir_stack[-1]["size"] += int(line[0])
            
def find_total(folder, ls):  # I suck at recursion but it works.
    result = 0 
    if len(folder) == 1:
        ls.append(folder["size"])
        return folder["size"]
        
    for k in folder:
        if k != "size":
            result += find_total(folder[k], ls)
    
    ls.append(result + folder["size"])
    return result + folder["size"]
    
total_ls = []

for folder in dir_sizes:
    find_total(dir_sizes[folder], total_ls)

answer = [i for i in total_ls if i <= 100000]
print(sum(answer))

# total space 70000000
# needed for update 30000000         

space_needed = (max(total_ls) + 30000000) - 70000000
for i in sorted(total_ls):
    if i >= space_needed:
        print(i)
        break

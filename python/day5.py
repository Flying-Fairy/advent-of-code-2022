with open("inputs/input5.txt") as f:
    cargos = []
    cargos_list = [[] for i in range(9)]
    
    for line in f.readlines():
        if "move" in line:
            line = [int(s) for s in line.split() if s.isdigit()]
            cargos.append(line)
        
        elif line != "\n":
            cargos.append(line)
    
        else:
            for i in range(len(cargos)):
                current = cargos.pop()
                index = 1
                for j in range(len(cargos_list)):
                    crate = current[index]
                    if crate != " ":
                        cargos_list[j].append(crate)
                    index += 4

for move in cargos:
    number, start, end = move
    moving_stack = []
    
    for i in range(number):
        current = cargos_list[start - 1].pop()
        moving_stack.insert(0, current)
    
    cargos_list[end - 1] += moving_stack

for stack in cargos_list:
    print(stack[-1], end="")
    
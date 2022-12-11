monkey_data = []
ROUNDS = 10000  # 20 for part 1

class Monkey:
    def __init__(self, start_item, operation, divisible_by, throw_target):
        
        self.inventory = start_item
        self.operation = operation
        self.divisible_by = divisible_by
        self.throw_target = throw_target
        
        self.inspected_item = 0
    
    def inspect(self, monkeys, divisor, modulo):
        if len(self.inventory) > 0:
            for _ in range(len(self.inventory)):
                item = self.inventory.pop(0)
                self.inspected_item += 1
                worry_level = None
                
                if self.operation[1] == "*":
                    if self.operation[2] == "old":
                        worry_level = item * item
                    else:
                        worry_level = item * int(self.operation[2])
                elif self.operation[1] == "+":
                    worry_level = item + int(self.operation[2]) 
                
                worry_level //= divisor
                
                if worry_level % self.divisible_by == 0:
                    if divisor == 1:
                        worry_level = worry_level % modulo
                    monkeys[self.throw_target[0]].inventory.append(worry_level)
                else:
                    monkeys[self.throw_target[1]].inventory.append(worry_level)


with open("day 11/input.txt") as f:
    data = []
    for line in f.readlines():
        if line == "\n":
            monkey_data.append(data)
            data = []
        else:
            data.append(line.strip())
    monkey_data.append(data)

monkeys = []

for data in monkey_data:
    starting_items = data[1].split(":")[1].split(",")
    starting_items = [int(i) for i in starting_items]
    
    operation = data[2].split("=")[1].split()
    
    divisible_by = int(data[3].split()[-1])
    
    target_monkey = []
    target_monkey.append(int(data[4].split()[-1]))
    target_monkey.append(int(data[5].split()[-1]))
    
    monkeys.append(Monkey(starting_items, operation, divisible_by, target_monkey))

lcm = 1
for monkey in monkeys:
    lcm *= monkey.divisible_by

for _ in range(ROUNDS):
    for monkey in monkeys:
        # monkey.inspect(monkeys, 3, lcm)
        monkey.inspect(monkeys, 1, lcm)
        
inspected_scores = []

for monkey in monkeys:
    inspected_scores.append(monkey.inspected_item)
    
inspected_scores = sorted(inspected_scores)
print(inspected_scores[-1] * inspected_scores[-2])

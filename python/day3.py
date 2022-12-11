from string import ascii_letters
from collections import Counter

with open("inputs/input3.txt", 'r') as f:
    bags = []
    for content in f:
        bags.append(content.replace("\n", ""))
        
letters = list(ascii_letters)

total_score = 0

for content in bags:
    mid = len(content) // 2
    c1 = Counter(content[:mid])
    c2 = Counter(content[mid:])

    for l in c1.keys():
        if l in c2:
            total_score += letters.index(l) + 1

print(total_score)

base_index = 0
total_score_2 = 0

for i in range(len(bags) // 3):
    
    for l in Counter(bags[base_index]):
        if l in Counter(bags[base_index + 1]):
            if l in Counter(bags[base_index + 2]):
                total_score_2 += letters.index(l) + 1

    base_index += 3

print(total_score_2)

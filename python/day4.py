pairs_countained = 0
pairs_overlap = 0

with open("inputs/input4.txt") as f:
    for line in f.readlines():
        pair1, pair2 = line.split(',')
        
        s1 = pair1.split('-')
        s2 = pair2.split('-')
        
        s1 = {i for i in range(int(s1[0]), int(s1[1]) + 1)}
        s2 = {i for i in range(int(s2[0]), int(s2[1]) + 1)}

        if s1.issubset(s2) or s2.issubset(s1):
            pairs_countained += 1
        
        overlap = s1 & s2        
        
        if overlap:
            pairs_overlap += 1

print(pairs_countained)
print(pairs_overlap)

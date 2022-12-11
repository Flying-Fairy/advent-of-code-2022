with open("inputs\input2.txt", 'r') as f:
    rps = []
    for line in f:
        rps.append(f"{line[0]} {line[2]}")
    

# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors 

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
LOSE = 0
DRAW = 3


moves = {
    "A X": ROCK + DRAW,
    "B X": ROCK + LOSE,
    "C X": ROCK + WIN,
    "A Y": PAPER + WIN,
    "B Y": PAPER + DRAW,
    "C Y": PAPER + LOSE,
    "A Z": SCISSORS + LOSE,
    "B Z": SCISSORS + WIN,
    "C Z": SCISSORS + DRAW
}

my_score = 0

for game in rps:
    my_score += moves[game]
            
print(my_score)  # solution for 1st part

# X: Lose, Y: Draw, Z: Win

moves_2 = {
    "A X": SCISSORS + LOSE,
    "B X": ROCK + LOSE,
    "C X": PAPER + LOSE,
    "A Y": ROCK + DRAW,
    "B Y": PAPER + DRAW,
    "C Y": SCISSORS + DRAW,
    "A Z": PAPER + WIN,
    "B Z": SCISSORS + WIN,
    "C Z": ROCK + WIN
}

my_score_2 = 0

for game in rps:
    my_score_2 += moves_2[game]

print(my_score_2)  # solution for 2nd part

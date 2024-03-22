
# read input.txt file and put it to an array

with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines] # python list comprehension

# ! Using Arrays
# ! Permutations

# A X --> R R = 1 + 3 = 4
# A Y --> R P = 1 + 0 = 1
# A Z --> R S = 1 + 6 = 7
# B X --> P R = 2 + 6 = 8
# B Y --> P P = 2 + 3 = 5
# B Z --> P S = 2 + 0 = 2
# C X --> S R = 3 + 0 = 3
# C Y --> S P = 3 + 6 = 9
# C Z --> S S = 3 + 3 = 6

# loop through every element of line
# use if else statements to compare the permutations
# have a variable that keeps track of the score
# after every if else statement, add the score to the score

score_array = 0
for line in lines:
    if line == "A X":
        score_array = score_array + 4
    elif line == "A Y":
        score_array = score_array + 1
    elif line == "A Z":
        score_array = score_array + 7
    elif line == "B X":
        score_array = score_array + 8
    elif line == "B Y":
        score_array = score_array + 5
    elif line == "B Z":
        score_array = score_array + 2
    elif line == "C X":
        score_array = score_array + 3
    elif line == "C Y":
        score_array = score_array + 9
    elif line == "C Z":
        score_array = score_array + 6

print('Score using array', score_array)

# ! Using Dictionaries:
# create a dictionary / hash map that contains the permutations

perm_to_score = {
    "A X": 4,
    "A Y": 1,
    "A Z": 7,
    "B X": 8,
    "B Y": 5,
    "B Z": 2,
    "C X": 3,
    "C Y": 9,
    "C Z": 6
}

score = 0
for line in lines:
    score = score + perm_to_score[line]
print('Score using dict', score)
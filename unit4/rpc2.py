
# read input.txt file and put it to an array

with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines] # python list comprehension

# homework
#status:     solved
#soluttion:  71502
f = open("input.txt", "r")

lines = f.readlines()

highest = 0
current = 0
for line in lines:
    if line == "\n":
        highest = max(highest, current)
        current = 0

    else:
        current += int(line);

print(highest)

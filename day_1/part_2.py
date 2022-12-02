#status:     solved
#soluttion:  208191 
f = open("input.txt", "r")

lines = f.readlines()

elves = []
current = 0
for line in lines:
    if line == "\n":
        elves.append(current)
        current = 0

    else:
        current += int(line);
total = 0
for i, elf in enumerate(sorted(elves, reverse=True)):
    if i < 3:
        total += elf
    else:
        print(total)
        exit(0) 
        


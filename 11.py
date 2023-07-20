f = open("jump_join_text.txt", "r")
output = []
for line in f:
    lines = line.split()
    if lines[0] == 'JOIN':
        output.append(lines[1])
    else:
        output.insert(0,lines[1])

print(*output, sep="\n")
f.close()
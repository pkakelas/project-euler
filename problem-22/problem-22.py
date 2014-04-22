file = open('problem-22/names.in', 'r')
names = file.read()
strings = names.split(",")

letters = [ 'A', 'B', 'C', 'D', 'R', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
names = scores = []

for name in strings:
    name = name.replace('"', '')
    if '\n' in name:
        name = name.replace('\n', '')
    names.append(name)

print names



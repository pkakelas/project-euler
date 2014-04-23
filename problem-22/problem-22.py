file = open('problem-22/names.in', 'r')
names = file.read()
strings = names.split(",")

letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
names = []
sum = 0

for name in sorted(strings):
    name = name.replace('"', '')
    if '\n' in name:
        name = name.replace('\n', '')
    names.append(name)

for name in names:
    nameScore = 0 
    for letter in name:
        nameScore += letters.index(letter) + 1
    sum += nameScore * (names.index(name) + 1)

print sum

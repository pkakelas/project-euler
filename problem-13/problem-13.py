file = open('problem-13/problem-13.in', 'r')

nums = []
for line in file:
    line = line.replace('\n', '')
    nums.append(int(line))

sum = 0
for num in nums:
    sum += num
    
print str(sum)[0:10]

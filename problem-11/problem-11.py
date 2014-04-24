file = open('problem-11/problem-11.in', 'r')

nums = []
king = 0 

for line in file:
    row = line.split(' ')
    row[-1] = row[-1].replace('\n', '')
    nums.append(row)

for line in nums:
    indexLine = nums.index(line)
    
    for num in line:
        try:    
            candidate = int(num) * int(line[indexLine + 1]) * int(line[indexLine + 2]) * int(line[indexLine + 3 ])
            if candidate > king:
                king = candidate
        except:
            break

    for num in line:
        indexNum = line.index(num)
        try:
            candidate = int(num) * int(nums[indexLine + 1][indexNum]) * int(nums[indexLine + 2][indexNum]) * int(nums[indexLine + 3][indexNum]) 
            if candidate > king:
                king = candidate    
        except:
            break
 
    for num in line:
        indexNum = line.index(num)
        try:
            candidate = int(num) * int(nums[indexLine + 1][indexNum + 1]) * int(nums[indexLine + 2][indexNum + 2]) * int(nums[indexLine + 3][indexNum + 3]) 
            if candidate > king:
                king = candidate    
        except:
            break
 
    for num in line:
        indexNum = line.index(num)
        try:
            candidate = int(num) * int(nums[indexLine - 1][indexNum + 1]) * int(nums[indexLine - 2][indexNum + 2]) * int(nums[indexLine - 3][indexNum + 3]) 
            if candidate > king:
                king = candidate    
        except:
            break

print king

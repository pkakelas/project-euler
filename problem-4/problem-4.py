def isPalindrome(num):
    chars = []
    for char in num:
        chars.append(char)
    inv = ''.join(num[::-1])
    if num == inv:
        return True

for num1 in range(100,1000):
    for num2 in range(100,1000):
        last = num1 * num2  
        if isPalindrome(str(last)):
            king = last
            
print king 

            

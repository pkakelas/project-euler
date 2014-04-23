nums = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def under100(num):
    array = list(str(num))
    if num < 100:
        if num < 20:
            return nums[num]
        if num % 10 == 0:
            return tens[int(array[0]) - 2]
        return tens[int(array[0]) - 2] + '-' + nums[int(array[1])]

def under1000(num):
    array = list(str(num))
    hundreds = nums[int(array[0])] + ' ' + 'hundred'

    if num % 100 == 0:
        return hundreds
    return hundreds + ' and ' + number(int(str(num)[1:]))

def number(num):
    if 1 <= num < 100:
        return under100(num)
    if 100 <= num <= 1000:
        return under1000(num)
        
def length(string):
    counter = 0
    for i in string:
        if '-' not in i:
            if i.isspace() != True:
                counter += 1
    return counter

counter = 0

for num in range(1, 1000):
    counter += length(number(num))
    print num 

print counter + length('one thousand')

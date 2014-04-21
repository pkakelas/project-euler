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
    return hundreds + ' and ' + under100(int(str(num)[1:]))

def under1000000(num):
    array = list(str(num))
    thousands = nums[int(array[0])] + ' ' + 'thousand'
    if num < 10000:
        if num % 1000 == 0:
            return thousands 
        return thousands + ' ' + number(int(''.join(array[1:])))
    if num < 100000:
        return number(int(''.join(array[0:2]))) + ' thousand ' + number(int(''.join(array[2:])))

def number(num):
    if num in range(1, 100):
        return under100(num)
    if num in range(100, 1000):
        return under1000(num)
    if num in range(1000, 1000000):
        return under1000000(num)
        
print number(7897)


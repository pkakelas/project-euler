def devides(num):
    for dividor in range(1, 21):
        if num % dividor != 0:
            return False
    return True

counter = 20
while True:
    if devides(counter):
        print counter
        break
    counter +=20



a, b = 0, 1
counter = 2

while True:
        c = a + b
        a = b
        b = c
        if len(list(str(c))) == 1000:
            print counter
            break
        counter += 1
        
        
        
        

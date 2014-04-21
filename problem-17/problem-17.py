n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19 = 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 8, 7, 9, 8, 8
n20, n30, n40, n50, n60, n70, n80, n90, n100, n1000, nmil = 6, 6, 5, 5, 5, 7, 6, 6, 7, 8, 7 

def lu100(num):
    num = list(str(num))
    first = 'n' + num[0] + '0'
    try:
        num[1]
    except:
        num = 'n' + num[0]
        return num 
    second = 'n' + num[1] 
    return first + second

print lu100(24)


def isPalindrome( num ):
    chars = []
    for char in num:
        chars.append( char )
    inv = ''.join( num[ ::-1 ] )
    if num == inv:
        return True

if isPalindrome( '1221' ):

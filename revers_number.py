# revers the order of number 
num = 12345
reversed = 0
while num > 0 :
    remainder = num % 10
    reversed = ( reversed * 10 )  + remainder
    num = num // 10
print( "reversed order of number: ", reversed )

# Check the palindrome number
num = 101
temp = num 
reversed = 0

while num > 0 :
    remainder = num % 10
    reversed = ( reversed * 10 )  + remainder
    num = num // 10
print("reversed:", reversed)

if reversed == temp :
    print("True")
else:
    print("False")


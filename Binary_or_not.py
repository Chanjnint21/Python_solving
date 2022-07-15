# Write program to check if it's binary numebrs

# methode 1
B_num = int(input("Enter binary number: "))
while B_num > 0 :
    remainder = B_num % 10
    if remainder < 2:
        binary = True
        B_num = B_num // 10
    if remainder > 1:
        binary = False
        print(" It's not binary number !")
        break
if binary == True :
    print("It's binary number ")

#methode 2

B_num = int(input("Enter binary number: "))
while B_num != 0 :
    remainder = B_num % 10
    if ( remainder != 0 and remainder != 1):
        print(" It's not binary number !")
        break
    B_num = B_num // 10
    if (B_num == 0):
        print("It's binary number ")
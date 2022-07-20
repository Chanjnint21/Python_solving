#write python to calculate factoria number

# Ask user to input number
number = int(input("Enter the number : "))
fac_num = 1

for i in range (1, number+1):
    fac_num = i * fac_num

print("The factorial of", number, "is", fac_num) 
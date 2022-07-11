# Find prime number between two number

def method1():
    amount = 0
    n1 = int(input("Input num 01: "))
    n2 = int(input("Input num 02: "))
    for num in range (n1, n2+1):
        if num > 1:
            for pn in range (2, num):
                if num % pn == 0:
                    break
            else:                                # each of for can use after break
                print(num)
                amount = amount +1
    print("1. Total of prime numbers:", amount)

# With all() funtion
def method2():
    amount = 0
    n1 = int(input("Input num 01: "))
    n2 = int(input("Input num 02: "))
    for num in range ( n1, n2):
        if num > 1:
            if all(num%i!=0 for i in range(2, num)):
                print(num)
                amount = amount + 1
    print("2. Total of prime numbers:", amount)


#Call funtion here
method1()
#method2()



